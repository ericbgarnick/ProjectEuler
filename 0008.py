from sys import argv
from typing import List

from maximums import n_consecutive_max


def read_collection(input_file_name: str) -> List[int]:
    raw_data = open(input_file_name, 'r').read().replace('\n', '')
    return [int(element) for element in raw_data]


if __name__ == '__main__':
    window_length = int(argv[1])
    input_file = argv[2]
    print(f"Max product for {window_length} digits in collection is "
          f"{n_consecutive_max(read_collection(input_file), window_length)}")
