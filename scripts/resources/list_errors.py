# ----------------------------------------------------------------------------------
# brief : List errors and output the list into the selected folder.
#
# author : l.heywang
# date : 10/09/2026
# ----------------------------------------------------------------------------------

# Imports
from pathlib import Path
import json


def list_errors(source: Path, target: Path):

    print("Dumping all of the errors... ")

    # First, get all the files :
    files = source.glob("*.err")

    # Second, open all the files and produce the file list
    output = dict()
    for file in files:

        lines = None
        with open(file, "r") as f:
            print((f"    ... Reading {file.name}"))
            lines = f.readlines()

        if len(lines) < 4:
            print(f"[ERROR] file {file.name} is not correctly formatted.")
            continue

        # Cleah the number into an integer. Easier to match.
        clean_hex = int(file.name.split(".")[0].removeprefix("0x"), 16)

        output[clean_hex] = {
            "url": lines[0].strip(),
            "name": lines[1].strip(),
            "cause": lines[2].strip(),
            "checks": lines[3].strip(),
        }

    # Dump this as JSON
    with open(target, "w+") as f:
        json.dump(output, f, ensure_ascii=True, indent=2)

    # Done
    return
