# Display options
# python -m pyserini.index.lucene -options

echo "Indexing WT2G collection... porter stemmer"

# porter stemmer (default)
python -m pyserini.index.lucene \
    --collection JsonCollection \
    --input data/collection \
    --index indexes/porter \
    --stemmer porter \
    --generator DefaultLuceneDocumentGenerator \
    --threads 1 \
    --storePositions --storeDocvectors --storeRaw

read -p "Press enter to continue"

echo "Indexing WT2G collection... krovet stemmer"

# krovetz stemmer
python -m pyserini.index.lucene \
    --collection JsonCollection \
    --input data/collection \
    --index indexes/krovetz \
    --stemmer krovetz \
    --generator DefaultLuceneDocumentGenerator \
    --threads 1 \
    --storePositions --storeDocvectors --storeRaw

read -p "Press enter to continue"

echo "Indexing WT2G collection... no stemmer"

# no stemmer
python -m pyserini.index.lucene \
    --collection JsonCollection \
    --input data/collection \
    --index indexes/none \
    --stemmer none \
    --generator DefaultLuceneDocumentGenerator \
    --threads 1 \
    --storePositions --storeDocvectors --storeRaw
