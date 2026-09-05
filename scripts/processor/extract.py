# ----------------------------------------------------------------------------------
# brief : Extract the N best words of the file
#
# author : l.heywang
# date : 05/09/2026
# ----------------------------------------------------------------------------------

# Imports
from pathlib import Path
from typing import Dict, List
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

# Defining the exclude list
FRENCH_STOPS = [
    "alors",
    "avec",
    "avoir",
    "cette",
    "comme",
    "dans",
    "donc",
    "elle",
    "elles",
    "encore",
    "etre",
    "faire",
    "mais",
    "meme",
    "nous",
    "parce",
    "peut",
    "plus",
    "pour",
    "sans",
    "sont",
    "sous",
    "tous",
    "tout",
    "tres",
    "vous",
    "qui",
    "par",
    "pas",
    "votre",
    "toi",
    "mon",
    "son",
    "autre",
    "dedans",
    "assez",
    "envies",
    "essentiel",
    "complexe",
    "clair",
    "impossible",
    "exhaustive",
    "jeff",
    "difficile",
]


def _clean(text: str) -> str:

    # Regex magic
    text = re.sub(r"^---[\s\S]*?---", "", text, flags=re.MULTILINE)
    text = re.sub(r"^---", "", text, flags=re.MULTILINE)
    text = re.sub(r"^(import|export)\s+.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\{/\*[\s\S]*?\*/\}", "", text)
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[*_#>`~|]", " ", text)

    return text


def _load(input: Path) -> str:

    # First, load the file content and clean it
    clean = ""
    with open(input, "r") as f:

        # First, clear the mdx files :
        data = f.read()

        # Clean the HTML / Astro / YAML syntax out of our way.
        clean = _clean(data)

    return clean


def _extract(input: list[dict], N: int) -> None:

    # First, load all of the elements :
    doc_ids = [x["src"].name for x in input]
    textList = [_load(x["src"]) for x in input]

    # Perform the TF-IDF operation
    print("Extracting TF-IDF...")
    vectorizer = TfidfVectorizer(
        stop_words=FRENCH_STOPS,
        token_pattern=r"(?u)\b[a-zA-Z0-9_-]{3,}\b",
        ngram_range=(1, 1),
        max_df=0.85,
        min_df=1,
        sublinear_tf=True,
    )

    # Fetch the matrix
    tfidf_matrix = vectorizer.fit_transform(textList)
    feature_names = np.array(vectorizer.get_feature_names_out())

    # Extract the keywords
    for idx, doc_id in enumerate(doc_ids):
        print(f"    ... Processing best words for {doc_id}")
        row = tfidf_matrix.getrow(idx).toarray().flatten()
        top_indices = np.argsort(row)[::-1]
        valid_indices = [i for i in top_indices if row[i] > 0][:N]
        input[idx]["extracted"] = feature_names[valid_indices].tolist()

    return
