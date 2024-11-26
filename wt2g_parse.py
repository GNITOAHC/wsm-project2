import json
import os

INPUT_DIR = "./WT2G/"
OUTPUT_FILE = "./data/collection/collections.jsonl"


count = 0


def parse_single_file(file_path):
    documents = []
    global count
    with open(file_path, "rb") as f:
        content = f.read().decode("utf-8", errors="ignore")
        raw_docs = content.split("<DOC>")[1:]
        raw_docs = ["<DOC>" + doc for doc in raw_docs]
        # print(f"Found {len(raw_docs)} documents in {file_path}")
        for doc in raw_docs:
            doc_id = doc.split("<DOCNO>")[1].split("</DOCNO>")[0].strip()
            documents.append({"id": doc_id, "contents": doc})
            count += 1
    return documents


def write_to_jsonl(documents):
    with open(OUTPUT_FILE, "a") as f:
        for doc in documents:
            f.write(json.dumps(doc) + "\n")
    pass


if __name__ == "__main__":
    for dirpath, dirnames, filenames in os.walk(INPUT_DIR):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            documents = parse_single_file(file_path)
            write_to_jsonl(documents)

    if count != 247491:
        print("Error: count != 247491")
        exit(1)
    # documents = parse_single_file(INPUT_DIR + "Wt01/B01")
    # print(count)
    # write_to_jsonl(documents)
