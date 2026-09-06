# ----------------------------------------------------------------------------------
# brief : Base handler for the global processing
#
# author : l.heywang
# date : 05/09/2026
# ----------------------------------------------------------------------------------

# Imports
from pathlib import Path
import hashlib
import tomllib
from datetime import datetime
from unidecode import unidecode

from .extract import _extract
from .keywords import _keywords
from .weights import _weight


def _get_data(input: Path) -> tuple[str, list[str], datetime, str, str, str]:

    print(f"Reading {str(input)} ...")

    out = hashlib.sha512()
    keywords = []
    date = None
    slug = ""
    title = ""
    author = ""

    with open(input, "rb") as f:

        # Fetch the data
        data = tomllib.load(f)
        out.update(data["slug"].encode())
        out.update(data["date"].encode())
        out.update(data["author"]["pseudo"].encode())

        # Fetch the keywords for a future extraction
        keywords.append(
            [
                unidecode(data["metadata"]["title_keyword"]),
                unidecode(data["author"]["pseudo"]),
            ]
        )
        keywords.append([unidecode(x) for x in data["metadata"]["aux_keywords"]])
        keywords.append([unidecode(x) for x in data["metadata"]["misc_keywords"]])

        # Extract the date
        date = datetime.strptime(data["date"], "%Y-%m-%d")

        # Extract the slug
        slug = data["slug"]

        # Extract the title and author
        title = unidecode(data["title"])
        author = unidecode(data["author"]["pseudo"])

    return out.hexdigest(), keywords, date, slug, title, author


def process(types: list[list[tuple[Path, Path]]]) -> list[dict]:

    # Flatten the list
    textList = []
    for doctype in types:
        textList.extend(doctype)

    print(f"Fetched {len(textList)} articles.")

    # Insert the hash ID
    fileList = []
    for text in textList:

        elements = dict()

        # Append elements
        sha, keywords, date, slug, title, author = _get_data(text[1])
        elements["hash"] = sha
        elements["toml"] = text[1]
        elements["src"] = text[0]
        elements["keywords"] = keywords
        elements["date"] = date
        elements["slug"] = slug
        elements["title"] = title
        elements["author"] = author

        fileList.append(elements)

    # Extract the best keywords
    _extract(fileList, 30)

    # Clean the keywords between all levels :
    print("Cleaning keywords ...")
    for index, file in enumerate(fileList):
        fileList[index] = _keywords(file)

    # Get the keywords and their weight metric :
    print("Computing the keywords weights ...")
    for index, file in enumerate(fileList):
        fileList[index] = _weight(file)

    return fileList
