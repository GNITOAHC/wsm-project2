read -p "extension: " ext
perl trec_eval.pl -q ./downloads/qrels.441-450 ./rankings/qrels_441_450/output.${ext} > ./rankings/qrels_441_450/result.${ext}
