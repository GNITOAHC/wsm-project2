# WSM Project 2: Building IR systems based on the Pyserini Project

## Data preparation:

**./WT2G/**

Download WT2G.tbz and extract to ./WT2G

**./data/collection/collections.jsonl**

1.  Create empty ./data/collection/collections.jsonl
2.  Run ./wt2g_parse.py

**./indexes/**

Run `sh wt2g_index.sh`

## File descriptions:

-   `wt2g_parse.py`: Parse ./WT2G to ./data/collection/collections.jsonl
    -   Create empty ./data/collection/collections.jsonl first
-   `trec_parse.py`: Export a parse function. Param `path` should be either `./downloads/trec10` or `./downloads/trec40`. Return list of {number, title}
    ```py
    def parse(path: str) -> list[tuple[str, str]]
    ```
-   `part1.py`: Generate ranked docs given the queries.
    -   Queries: Generated from `trec_parse.py`
-   `trec_eval.sh`: Evaluate the results from `./rankings/{eval_path}/{searcher}/output.{index}`
    -   eval_path: "qrels_401_440" or "qrels_441_450"
    -   searcher: "bm25", "lmmle" or "lmjm"
    -   index: "porter", "krovetz" or "none"
    -   Calling `./trec_eval.pl` under the hood.
        ```
        perl trec_eval.pl -q qrels.401-404 {generated_output} > {output_path}
        ```
-   `./rankings/plot/`: Script to plot results
-   `./rankings/qrels_441_450/map.py`, `./rankings/qrels_441_450/p10.py`: Script to plot results
