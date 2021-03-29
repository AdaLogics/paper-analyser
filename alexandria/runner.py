"""
Usage:
    runner.py <folder>
"""
import os
from docopt import docopt
from bs4 import BeautifulSoup
from grobid_client.grobid_client import GrobidClient
from pqlib import Article

# Valid grobid services
FULL = "processFulltextDocument"
HEADER = "processHeaderDocument"
REFS = "processReferences"


def parse_pdf(client, pdf_file):
    _, status, r = client.process_pdf(service=FULL,
                                      pdf_file=pdf_file,
                                      generateIDs=False,
                                      consolidate_header=True,
                                      consolidate_citations=False,
                                      include_raw_citations=False,
                                      include_raw_affiliations=False,
                                      teiCoordinates=True,
                                     )

    return Article(BeautifulSoup(r, "lxml"))


if __name__ == "__main__":
    args = docopt(__doc__)

    grobid = GrobidClient("./grobid_config.json")

    for pdf_file in os.listdir(args["<folder>"]):
        if not pdf_file.endswith(".pdf"):
            continue
        print(pdf_file)
        a = parse_pdf(grobid, os.path.join(args["<folder>"], pdf_file))
        print(a.to_json())
