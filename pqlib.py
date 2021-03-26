"""Contains the data structures and parsing functions to process
and store data contained in an academic article.
"""
import re
from bs4 import BeautifulSoup


def text(field):
    return field.text.strip() if field else ""
    

class Author:
    """Contains information about an author.
    """
    def __init__(self, soup):
        """Creates an `Author` by parsing a `soup` of type
        `BeautifulSoup`.
        """
        self.name = text(soup.persname.forename)
        self.surname = text(soup.persname.surname)
        # TODO: better affiliation parsing.
        self.affiliation = list(map(text, soup.find_all("affiliation")))

    def __str__(self):
        s = ""
        if self.name:
            s += self.name + " "
        if self.surname:
            s += self.surname

        return s.strip()

class Article:
    """Represents an academic article or a reference contained in
    an article.

    The data is parsed from a TEI XML file (`from_file()`) or
    directly from a `BeautifulSoup` object.
    """
    def __init__(self, soup, is_reference=False):
        """Create a new `Article` by parsing a `soup: BeautifulSoup`
        instance.
        The parameter `is_reference` specifies if the `soup` contains
        an entire article or just the content of a reference.
        """
        self.title = text(soup.title)
        self.doi = text(soup.idno)
        self.abstract = text(soup.abstract)
        # FIXME
        self.year = None

        if is_reference:
            self.authors = list(map(Author, soup.find_all("author")))
        else:
            self.authors = list(map(Author, soup.analytic.find_all("author")))
            self.references = self._parse_biblio(soup)

    @staticmethod
    def from_file(self, tei_file):
        """Creates an `Article` by parsing a TEI XML file.
        """
        if soup is None:
            if tei_file is None:
                raise Exception("Please provide either `tei_file` or `soup`)")
            with open(tei_file) as f:
                soup = BeautifulSoup(f, "lxml")

        return Article(soup)

    def _parse_biblio(self, soup):
        """Parses the bibliography from an article.
        """
        references = []
        # NOTE: we could do this without the regex.
        bibs = soup.find_all("biblstruct", {"xml:id": re.compile(r"b[0-9]*")})

        for bib in bibs:
            if bib.analytic:
                references.append(Article(bib.analytic, is_reference=True))
                # NOTE: in this case, bib.monogr contains more info
                # about the manuscript where the paper was published.
                # Not parsing for now.
            elif bib.monogr:
                references.append(Article(bib.monogr, is_reference=True))
            else:
                print(f"Could not parse reference from {bib}")

        return references

    def __str__(self):
        return f"'{self.title}' - {' '.join(map(str, self.authors))}"
