# ----------------------------------------------------------------------------------
# brief : List files from the ressources public folder, and enable helper to
#         access them !
#
# author : l.heywang
# date : 08/09/2026
# ----------------------------------------------------------------------------------

# Imports
from pathlib import Path
import json


def list_resources(source: Path, target: Path):

    print("Dumping all of the resources files... ")

    # First, get all the files :
    files = source.glob("*")
    output = [file.name for file in files]

    # Dump this as JSON
    with open(target, "w+") as f:
        json.dump(output, f, ensure_ascii=True, indent=2)

    # Done
    return
