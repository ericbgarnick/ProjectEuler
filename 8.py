import math
from sys import argv


def read_collection(input_file_name: str) -> str:
    return open(input_file_name, 'r').read().replace('\n', '')


def n_consecutive_max(collection: str, n: int):
    """Return the maximum product of n consecutive digits in collection."""
    collection = [int(element) for element in collection]
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


if __name__ == '__main__':
    window_length = int(argv[1])
    input_file = argv[2]
    print(f"Max product for {window_length} digits in collection is "
          f"{n_consecutive_max(read_collection(input_file), window_length)}")
