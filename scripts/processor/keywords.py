# ----------------------------------------------------------------------------------
# brief : Process the keywords and ensure no duplicates
#
# author : l.heywang
# date : 05/09/2026
# ----------------------------------------------------------------------------------

# Imports
from unidecode import unidecode

def _remove(inp: list[str], stop: list[str]) -> tuple[list[str], list[str]]:

    localStop = stop
    output = []

    for word in inp:

        temp = unidecode(word).lower()

        # Is the word already seen ? 
        if temp in localStop:
            continue
        else:

            # Does the word match a pattern we already seen ? 
            if temp.endswith("s") or temp.endswith("x"):
                if temp[:-1] in localStop:
                    continue

            output.append(temp)
            localStop.append(temp)

    return localStop, output

def _keywords(inp: dict):

    # Extract the different keywords
    L1 = inp["keywords"][0]
    L2 = inp["keywords"][1]
    L3 = inp["keywords"][2]
    L4 = inp["extracted"]

    # Ensure we won't pass a reference and modify L1...
    stopList = [] 
    stopList.extend([Lx.lower() for Lx in L1])

    # Clean the keywords
    stopList, L2 = _remove(L2, stopList)
    stopList, L3 = _remove(L3, stopList)
    stopList, L4 = _remove(L4, stopList)

    # Output the data back
    inp["L1"] = [Lx.lower() for Lx in L1]
    inp["L2"] = [Lx.lower() for Lx in L2]
    inp["L3"] = [Lx.lower() for Lx in L3]
    inp["L4"] = [Lx.lower() for Lx in L4]

    # Clean the original variables
    del inp["extracted"]
    del inp["keywords"]

    return inp



    
