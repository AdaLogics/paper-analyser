# Simple example

We include two whitepapers in the repository as examples for using
paper-analyser to pass papers and get results out.

To try the tool, simply follow the commands:
```
cd paper-analyzer
. venv/bin/activate
python3 ./pq_main.py -f ./example-papers/
```

At this point you will see results in `pq-out/out-0`

Specifically, you will see:
```
$ ls pq-out/out-0/
data_out  img  json_data  normalised_dependency_graph.json  parsed_paper_data.json
```

* `data_out` contains one `.txt` and one `.xml` file for each PDF. These `.txt` and `.xml` are simply data representations of the content of the given PDF file.
* `json_data` contains JSON data representations for each paper
* `img` contains a `.png` image of a citation-dependency graph of the PDF files in the folder
* `parsed_paper_data.json` is a single json file containing data about the papers analysed, such as the title of each paper as well as the papers cited by each paper.

