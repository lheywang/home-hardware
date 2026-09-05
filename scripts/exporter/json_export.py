# ----------------------------------------------------------------------------------
# brief : Export the buffer to the JSON format
#
# author : l.heywang
# date : 05/09/2026
# ----------------------------------------------------------------------------------

# Imports
import json
from pathlib import Path
from dataclasses import asdict, dataclass
import time

def export(target: Path, data: list[dict]) -> None:

    # Clean up the elements
    for index, buf in enumerate(data):
        del data[index]["src"]
        del data[index]["toml"]

        data[index]["date"] = buf["date"].timestamp()

    # For the buffer as required now
    print("Building JSON structure ...")
    payload = dict()
    payload["timestamp"] = int(time.time())
    payload["version"] = 1
    payload["count"] = len(data)
    payload["data"] = data

    # Encode the buffer into JSON
    print("Writting file ...")
    with open(target, "w+") as f:
        json.dump(
            payload, 
            f, 
            ensure_ascii=True, 
            indent=2
        )

    return


