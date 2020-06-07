import math
from typing import List


def n_consecutive_max(collection: List[int], n: int):
    """Return the maximum product of n consecutive digits in collection."""
    next_idx = n
    best_product = cur_product = math.prod(collection[:n])
    while next_idx < len(collection):
        if cur_product:
            cur_product *= collection[next_idx] / collection[next_idx - n]
        else:
            cur_product = math.prod(collection[next_idx - n + 1:next_idx + 1])
        best_product = max(best_product, cur_product)
        next_idx += 1
    return int(best_product)
