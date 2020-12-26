# Example of larger analyses

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

