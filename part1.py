from pyserini.search.lucene import LuceneSearcher
from pyserini.pyclass import autoclass
from trec_parse import parse
import argparse
import os

# Similarity classes
LMSimilarity = autoclass("org/apache/lucene/search/similarities/LMSimilarity")
LMJelinekMercerSimilarity = autoclass(
    "org/apache/lucene/search/similarities/LMJelinekMercerSimilarity"
)
LMDirichletSimilarity = autoclass(
    "org/apache/lucene/search/similarities/LMDirichletSimilarity"
)
DFRSimilarity = autoclass("org/apache/lucene/search/similarities/DFRSimilarity")

# AfterEffect classes
AfterEffectL = autoclass("org/apache/lucene/search/similarities/AfterEffectL")

# Model classes
BasicModelG = autoclass("org/apache/lucene/search/similarities/BasicModelG")
BasicModelIF = autoclass("org/apache/lucene/search/similarities/BasicModelIF")
BasicModelIn = autoclass("org/apache/lucene/search/similarities/BasicModelIn")
BasicModelIne = autoclass("org/apache/lucene/search/similarities/BasicModelIne")

# Normalization classes
NormalizationH1 = autoclass("org/apache/lucene/search/similarities/NormalizationH1")
NormalizationH2 = autoclass("org/apache/lucene/search/similarities/NormalizationH2")
NormalizationH3 = autoclass("org/apache/lucene/search/similarities/NormalizationH3")
NormalizationZ = autoclass("org/apache/lucene/search/similarities/NormalizationZ")

IndexSearcher = autoclass("org.apache.lucene.search.IndexSearcher")


class DFRSearcher(LuceneSearcher):
    def custom_qld(self, bm, ae, normalization):
        self.object.similarity = DFRSimilarity(bm, ae, normalization)
        self.object.searcher = IndexSearcher(self.object.reader)
        self.object.searcher.setSimilarity(self.object.similarity)


class LMJelinekMercerSearcher(LuceneSearcher):
    def set_qld(self, mu=float(1000)):
        self.object.similarity = LMJelinekMercerSimilarity(mu)
        self.object.searcher = IndexSearcher(self.object.reader)
        self.object.searcher.setSimilarity(self.object.similarity)
        # searcher = new IndexSearcher(reader);
        # searcher.setSimilarity(similarity);


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--index", type=str, default="porter", help="{porter, krovetz, none}"
    )
    parser.add_argument(
        "--searcher", type=str, default="bm25", help="{bm25, lmmle, lmjm}"
    )
    parser.add_argument(
        "--eval", type=int, help="40(qrels.401-440) or 10(qrels.441-450)", default=40
    )
    args = parser.parse_args()

    eval = "qrels_401_440" if args.eval == 40 else "qrels_441_450"
    parse_target = "./downloads/trec40" if args.eval == 40 else "./downloads/trec10"
    target_file = f"./rankings/{eval}/{args.searcher}/output.{args.index}"
    os.makedirs(f"./rankings/{eval}/{args.searcher}", exist_ok=True)

    index = f"indexes/{args.index}"
    searcher = None
    match args.searcher:
        case "bm25":
            searcher = LuceneSearcher(index)
            searcher.set_bm25(k1=1.2, b=0.75)
        case "lmmle":
            # searcher = LMMLELaplaceSearcher(index)
            searcher = LuceneSearcher(index)
            searcher.set_qld()
        case "lmjm":
            searcher = LMJelinekMercerSearcher(index)
            searcher.set_qld(0.8)
        case "dfr-g-l-h2":
            searcher = DFRSearcher(index)
            searcher.custom_qld(BasicModelG(), AfterEffectL(), NormalizationH2())
        case "dfr-in-l-h1":
            searcher = DFRSearcher(index)
            searcher.custom_qld(BasicModelIn(), AfterEffectL(), NormalizationH1())
        case "dfr-in-l-h2":
            searcher = DFRSearcher(index)
            searcher.custom_qld(BasicModelIn(), AfterEffectL(), NormalizationH2())
        case "dfr-in-l-h3":
            searcher = DFRSearcher(index)
            searcher.custom_qld(BasicModelIn(), AfterEffectL(), NormalizationH3())
        case "dfr-in-l-z":
            searcher = DFRSearcher(index)
            searcher.custom_qld(BasicModelIn(), AfterEffectL(), NormalizationZ())
        case "dfr-ine-l-h2":
            searcher = DFRSearcher(index)
            searcher.custom_qld(BasicModelIne(), AfterEffectL(), NormalizationH2())
        case _:
            print("Invalid searcher")
            exit(1)

    parsed = parse(parse_target)
    with open(target_file, "w") as f:
        for p in parsed:
            hits = searcher.search(f"{p[0]}. {p[1]}", 1000)
            for i in range(len(hits)):
                if hits[i].score <= 0.0:
                    break
                # print(f"{p[0]} Q0 {hits[i].docid} {i+1} {hits[i].score:.5f} bm25")
                f.write(
                    f"{p[0]} Q0 {hits[i].docid} {i+1} {hits[i].score:.5f} {args.searcher}\n"
                )

    # query = """foreign minorities, Germany"""

    # hits = searcher.search("401. foreign minorities, germany", 1000)
    # hits = searcher.search(query)

    # for i in range(len(hits)):
    #     print(f"401 Q0 {hits[i].docid} {i+1} {hits[i].score:.5f} bm25")
