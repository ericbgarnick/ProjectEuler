from sys import argv
from typing import Tuple, List


def pyth_triplet(target: int) -> List[Tuple[int, int, int]]:
    squares = {root: root * root for root in range(target)}
    triplets = []
    c = target - 3
    while c > 2:
        c -= 1
        c_sq = squares[c]
        max_b = target - c - 2
        min_b = int(max_b / 2)
        for b in range(min_b, max_b + 1):
            a = target - c - b
            a_sq = squares[a]
            b_sq = squares[b]
            if a_sq + b_sq == c_sq:
                triplets.append((a, b, c))
    return triplets


if __name__ == '__main__':
    start_value = int(argv[1])
    print(pyth_triplet(start_value))
