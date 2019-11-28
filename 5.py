import json
from collections import defaultdict
from sys import argv
from typing import Dict


# {num: {factor: count}}
FACTORED = {}


def prime_factors(num: int) -> defaultdict:
    original = num
    factors = defaultdict(int)  # {factor: count}
    f = 2
    while f <= num:
        if num in FACTORED:
            for k, v in FACTORED[num].items():
                factors[k] += v
            # Done
            f = num + 1
        else:
            div, rem = divmod(num, f)
            if rem:
                # Not a factor. Keep looking
                f += 1
            else:
                # Found a factor. Record and restart with div
                factors[f] += 1
                num = div
                f = 2
    FACTORED[original] = factors
    return factors


def merge_factors() -> Dict[int, int]:
    result = {}
    for num, factor_dict in FACTORED.items():
        for f, c in factor_dict.items():
            result[f] = max(result.get(f, 0), c)
    return result


def multiply_factors(to_mult: Dict[int, int]) -> int:
    total = 1
    for f, c in to_mult.items():
        total *= f ** c
    return total


def pp(d: Dict):
    print(json.dumps(d, indent=4, sort_keys=True))


if __name__ == '__main__':
    start_num = int(argv[1])

    for start in range(start_num, 1, -1):
        factor = prime_factors(start)

    merged = merge_factors()
    print(f"Result: {multiply_factors(merged)}")
