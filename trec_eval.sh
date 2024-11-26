#!/bin/bash

read -p "index (porter, krovetz, none): " index
read -p "searcher (bm25, lmmle, lmjm): " searcher
read -p "qrel (40, 10): " qrel

qrel_src=""
qrel_out_dir=""
if [ $qrel -eq 40 ]; then
    qrel_src="qrels.401-440"
    qrel_out_dir="qrels_401_440"
else
    qrel_src="qrels.441-450"
    qrel_out_dir="qrels_441_450"
fi

echo "\nindex: $index, searcher: $searcher, qrel: $qrel"

src="./rankings/${qrel_out_dir}/${searcher}/output.${index}"
target="./rankings/${qrel_out_dir}/${searcher}/result.${index}"

echo ${src}
echo ${target}

read -p "Run trec_eval? (y/n): " run
if [ $run == "n" ]; then
    echo "Stopping..."
    exit 1
fi

# echo "Run script"
# echo "perl trec_eval.pl -q ./downloads/${qrel_src} ${src} > ${target}"
perl trec_eval.pl -q ./downloads/${qrel_src} ${src} > ${target}
