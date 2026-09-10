# ----------------------------------------------------------------------------------
# brief : List the links to be used for the helpers
#
# author : l.heywang
# date : 10/09/2026
# ----------------------------------------------------------------------------------

# Imports
from pathlib import Path
import json


def list_links(source: Path, target: Path):

    print("Dumping all of the errors... ")

    # First, get all the files :
    files = source.glob("*.url")

    # Second, open all the files and produce the file list
    output = dict()
    for file in files:

        line = None
        with open(file, "r") as f:
            print(f"    ... Reading {file}")
            line = f.readline()

        output[file.name.split(".")[0]] = line

    # Dump this as JSON
    with open(target, "w+") as f:
        json.dump(output, f, ensure_ascii=True, indent=2)

    # Done
    return
