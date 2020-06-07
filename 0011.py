from sys import argv
from typing import List

from maximums import n_consecutive_max

Grid = List[List[int]]


WINDOW_SIZE = 4


def greatest_product(input_data: Grid) -> int:
    horizontals = input_data
    verticals = create_verticals(input_data)
    desc_diag = create_desc_diag(input_data)
    asc_diag = create_asc_diag(input_data)

    best_product = 0

    for grid in [horizontals, verticals, desc_diag, asc_diag]:
        for row in grid:
            if len(row) >= WINDOW_SIZE:
                best_product = max(best_product, n_consecutive_max(row, WINDOW_SIZE))
    return best_product


def create_verticals(input_data: Grid) -> Grid:
    size = len(input_data)
    verticals = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            verticals[i][j] = input_data[j][i]
    return verticals


def create_desc_diag(input_data: Grid) -> Grid:
    size = len(input_data)
    desc_diag = []
    # Bottom left up to top left
    for start_row in range(size - 1, -1, -1):
        cur_row = start_row
        cur_col = 0
        desc_diag.append([])
        while cur_row < size:
            cur_elem = input_data[cur_row][cur_col]
            desc_diag[-1].append(cur_elem)
            cur_row += 1
            cur_col += 1
    # Top left over to top right
    for start_col in range(1, size):
        cur_col = start_col
        cur_row = 0
        desc_diag.append([])
        while cur_col < size:
            cur_elem = input_data[cur_row][cur_col]
            desc_diag[-1].append(cur_elem)
            cur_row += 1
            cur_col += 1
    return desc_diag


def create_asc_diag(input_data: Grid) -> Grid:
    size = len(input_data)
    asc_diag = []
    # Top left down to bottom left
    for start_row in range(size):
        cur_row = start_row
        cur_col = 0
        asc_diag.append([])
        while cur_row > -1:
            cur_elem = input_data[cur_row][cur_col]
            asc_diag[-1].append(cur_elem)
            cur_row -= 1
            cur_col += 1
    # Bottom left over to bottom right
    for start_col in range(1, size):
        cur_col = start_col
        cur_row = size - 1
        asc_diag.append([])
        while cur_col < size:
            cur_elem = input_data[cur_row][cur_col]
            asc_diag[-1].append(cur_elem)
            cur_row -= 1
            cur_col += 1
    return asc_diag


if __name__ == '__main__':
    input_file = argv[1]
    data_grid = []
    with open(input_file, 'r') as f_in:
        for line in f_in:
            data_grid.append([int(elem) for elem in line.strip().split()])

    print(f"Max product for window of size {WINDOW_SIZE}: {greatest_product(data_grid)}")
