# ----------------------------------------------------------------------------------
# brief : Compute the weight of the different tokens.
#
# author : l.heywang
# date : 05/09/2026
# ----------------------------------------------------------------------------------

# Configuration
L1_MAX = 100000
L1_MIN = 50000
L1_STP = (L1_MAX - L1_MIN) // (1 - 1)

L2_MAX = 10000
L2_MIN = 5000
L2_STP = (L2_MAX - L2_MIN) // (4 - 1)

L3_MAX = 1000
L3_MIN = 500
L3_STP = (L3_MAX - L3_MIN) // (6 - 1)

L4_MAX = 100
L4_MIN = 1
L4_STP = (L4_MAX - L4_MIN) // (30 - 1)

def _get_value(idx: int, maxval: int, min: int, step: int) -> int:
    return round(max(maxval - (idx * step), min))

def _get_weight(inp: list[str], max: int, min: int, step: int) -> list[tuple[str, int]]:

    output = []
    for index, word in enumerate(inp):
        output.append((word, _get_value(index, max, min, step)))

    return output

def _weight(inp: dict):

    # Get the weight for the different levels
    tokens = []

    # Get the different weights tupples
    tokens.extend(_get_weight(inp["L1"], L1_MAX, L1_MIN, L1_STP))
    tokens.extend(_get_weight(inp["L2"], L2_MAX, L2_MIN, L2_STP))
    tokens.extend(_get_weight(inp["L3"], L3_MAX, L3_MIN, L3_STP))
    tokens.extend(_get_weight(inp["L4"], L4_MAX, L4_MIN, L4_STP))

    # Add the data to the dict
    inp["tokens"] = dict(tokens)

    # Clean the previous lists
    del inp["L1"]
    del inp["L2"]
    del inp["L3"]
    del inp["L4"]

    return inp
