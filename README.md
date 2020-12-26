# Paper analyser
The goal of this project is to enable quantitative analysis of 
academic papers. 

To achieve the goal, the project contains logic for

1. Parsing academic white papers into structured representation
1. Doing analysis on the structured representations

The project as it currently stands focuses on the task of taking 
a list of arbitrary papers in the form of PDFs, and then creating
a dependency graph of citations amongst these papers. This graph
then shows how each of the PDFs reference each other.

To achieve the above task, various tasks are are needed, e.g. :

1. parsing the papers to extract citations,
   1. Read the PDF files to a format usable in Python
   1. Extract (1) title and (2) citations of a given paper
   1. For each citation in the paper:
      1. Extract the (1) title and (2) authors of the citation
1. Normalise the extracted citations
1. Do some dependency analysis based on the above citation extractions

## Installation
```
git clone https://github.com/AdaLogics/paper-analyser
cd paper-analyser
./install.sh
```

## Usage 
### Example usage
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

### Getting larger paper lists
Paper analyser relies on PDF file representations of academic papers.
As such, it is up to you to find these papers. 

For convenience we maintain a list of links to software analysis papers
focused on software security in our sister repository [here](https://github.com/AdaLogics/software-security-paper-list)

As an example of doing analysis on several Fuzzing papers, you can use the following commands:

```
cd paper-analyzer
mkdir tmp && cd tmp
git clone https://github.com/AdaLogics/software-security-paper-list
cd software-security-paper-list
python auto_download.py Fuzzing
```

At this point you will see more than 80 papers in the directory `out/Fuzzing/`

We continue to do analysis on these papers:
```
cd ../..
python3 pq_main.py -f ./tmp/software-security-paper-list/out/Fuzzing
```



## Contribute
We welcome contributions. 

Paper analyser is maintained by Ada Logics, including: 
* [David Korczynski](https://twitter.com/Davkorcz)  
* [Adam Korczynski](https://twitter.com/AdamKorcz4)

We are particularly interested in features for:
1. Improved parsing of the PDF files to get better structured ouput out
1. More data analysis into the project


### Feature suggestions
If you would like to contribute but dont have a feature in mind, please see the list below for suggestions:

* Extraction of authors from papers
* Extractino of the actual text from the papers. This could be used for a lot of cool data analysis
