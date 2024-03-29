"""
Usage:
    runner.py <folder>
"""
import os
import sys
import pymongo
from docopt import docopt
from bs4 import BeautifulSoup
from grobid_client.grobid_client import GrobidClient

from base import Article

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

    grobid = GrobidClient("./grobid.json")
    client = pymongo.MongoClient("localhost", 27017)
    print("Connecting to db.")
    try:
        client.server_info()
    except pymongo.errors.ServerSelectionTimeoutError:
        print("Failed to connect to db.")
        sys.exit(1)

    db = client.alexandria

    print(f"Processing files in {args['<folder>']}")

    for pdf_file in os.listdir(args["<folder>"]):
        if not pdf_file.endswith(".pdf"):
            continue
        print(f"Parsing {pdf_file}")
        article = parse_pdf(grobid, os.path.join(args["<folder>"], pdf_file))
        # Can also do print(a.to_json())
        article.summary()
        print()

        db.articles.insert_one(article.to_dict())
