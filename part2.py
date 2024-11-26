import argparse
from enum import Enum
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler, RobustScaler


class Scaler(Enum):
    NONE = 0
    MINMAX = 1
    ROBUST = 2


class Features(Enum):
    """{searcher}_{index}"""

    BM25__PORTER = 0
    BM25__KROVETZ = 1
    BM25__NONE = 2
    LMMLE__PORTER = 3
    LMMLE__KROVETZ = 4
    LMMLE__NONE = 5
    LMJM__PORTER = 6
    LMJM__KROVETZ = 7
    LMJM__NONE = 8
    DFR_IN_L_H3__PORTER = 9
    DFR_IN_L_Z__PORTER = 10


def features_desc() -> str:
    return ", ".join([f"{f.name.lower()}" for f in Features])


def get_features(features) -> list[Features]:
    """e.g. 0b001010100 -> [BM25_NONE, LMMLE_KROVETZ, LMJM_PORTER]"""
    enabled = []
    f_count = len(Features)
    for f in Features:
        bit_pos = f_count - 1 - f.value
        if features & (1 << bit_pos):
            enabled.append(f)
    return enabled


def paths(features: list[Features], qrels) -> list[str]:
    """
    ./rankings/qrels_401_440/{searcher}/output.{index}
    ./rankings/qrels_441_450/{searcher}/output.{index}
    """
    qrels_range = ""
    if qrels == 40:
        qrels_range = "401_440"
    else:
        qrels_range = "441_450"
    _paths = [
        f"./rankings/qrels_{qrels_range}/{feature.name.split('__')[0].lower().replace('_', '-')}/output.{feature.name.replace('__', ' ').split(' ')[1].lower()}"
        for feature in features
    ]
    return _paths


def labels(features: list[Features]) -> list[str]:
    """{searcher}_{index} for searcher in [bm25, lmmle, lmjm] for index in [porter, krovetz, none]"""
    return [feature.name.lower() for feature in features]


qrels_path = "./downloads/qrels.401-440"


def create_dataframe(features: list[Features], normalize: Scaler):
    qrel_headers = ["query_id", "_", "doc_id", "relevance"]
    df_qrels = pd.read_csv(qrels_path, sep=" ", header=None, names=qrel_headers)

    ranking_headers = ["query_id", "_", "doc_id", "rank", "score", "searcher"]
    df_rankings = pd.DataFrame()
    for path in paths(features, 40):
        index = path.split("/")[-1].split(".")[1]  # porter, krovetz, none
        searcher = path.split("/")[-2].replace("-", "_")  # bm25, lmmle, lmjm, dfr_in_l_h3

        # print(searcher + "__" + index)
        # print(path)

        rankings = pd.read_csv(path, sep=" ", header=None, names=ranking_headers)
        rankings["searcher"] = f"{searcher}__{index}"
        df_rankings = pd.concat([df_rankings, rankings])

    df_pivot = df_rankings.pivot_table(
        index=["query_id", "doc_id"], columns="searcher", values="score"
    ).reset_index()

    df_merged = pd.merge(df_qrels, df_pivot, on=["query_id", "doc_id"], how="inner")
    df_merged = df_merged[["query_id", "doc_id"] + labels(features) + ["relevance"]]

    match normalize:
        case Scaler.MINMAX:
            for f in labels(features):
                df_merged[f] = MinMaxScaler().fit_transform(df_merged[[f]])
        case Scaler.ROBUST:
            for f in labels(features):
                df_merged[f] = RobustScaler().fit_transform(df_merged[[f]])
        case Scaler.NONE:
            pass

    relevance = df_merged.pop("relevance")
    df_merged["relevance"] = relevance

    df_merged.fillna(0, inplace=True)

    # print(df_merged)
    return df_merged


def create_test_dataframe(features: list[Features], normalize: Scaler):
    testing_headers = ["query_id", "_", "doc_id", "rank", "score", "searcher"]
    df_testings = pd.DataFrame()
    for path in paths(features, 10):
        index = path.split("/")[-1].split(".")[1]  # porter, krovetz, none
        searcher = path.split("/")[-2].replace("-", "_")  # bm25, lmmle, lmjm

        testings = pd.read_csv(path, sep=" ", header=None, names=testing_headers)
        testings["searcher"] = f"{searcher}__{index}"
        df_testings = pd.concat([df_testings, testings])

    df_pivot = df_testings.pivot_table(
        index=["query_id", "doc_id"], columns="searcher", values="score"
    ).reset_index()

    df_pivot = df_pivot[["query_id", "doc_id"] + labels(features)]

    match normalize:
        case Scaler.MINMAX:
            for f in labels(features):
                df_pivot[f] = MinMaxScaler().fit_transform(df_pivot[[f]])
        case Scaler.ROBUST:
            for f in labels(features):
                df_pivot[f] = RobustScaler().fit_transform(df_pivot[[f]])
        case Scaler.NONE:
            pass

    df_pivot.fillna(0, inplace=True)

    return df_pivot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--features",
        type=lambda x: int(x, 0),
        help=f"Feature indexes (bitmask): {features_desc()}",
        default=0b111111111,
    )
    parser.add_argument("-e", "--ext", type=str, help="File extension", default="tmp")
    parser.add_argument(
        "-s", "--scaler", type=str, help="Normalization: minmax, robust", default="none"
    )
    args = parser.parse_args()
    features = get_features(args.features)
    print(features)

    normalize = Scaler.NONE
    match args.scaler:
        case "minmax":
            normalize = Scaler.MINMAX
        case "robust":
            normalize = Scaler.ROBUST
        case _:
            pass

    df = create_dataframe(features, normalize)
    print(df)
    df_test = create_test_dataframe(features, normalize)
    print(df_test)

    # exit(0)

    _labels = labels(features)

    model = RandomForestClassifier()
    model.fit(df[_labels], df["relevance"])

    predictions = model.predict_proba(df_test[_labels])

    df_predicted = pd.DataFrame(
        {
            "query_id": df_test["query_id"],
            "doc_id": df_test["doc_id"],
            "score": [p[1] for p in predictions],
        }
    )
    df_predicted = df_predicted.sort_values(
        by=["query_id", "score"], ascending=[True, False]
    )
    df_predicted = df_predicted[df_predicted["score"] > 0.0]
    df_predicted = df_predicted.groupby("query_id").head(1000)
    df_predicted["rank"] = df_predicted.groupby("query_id").cumcount() + 1

    with open(f"./rankings/qrels_441_450/output.{args.ext}", "w") as f:
        for _, row in df_predicted.iterrows():
            f.write(
                f"{row['query_id']} Q0 {row['doc_id']} {row['rank']} {row['score']:.5f} rf\n"
            )


if __name__ == "__main__":
    main()
