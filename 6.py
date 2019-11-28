from sys import argv


def cheat(top: int) -> int:
    sum_sq = sum(i * i for i in range(top + 1))
    sq_sum = sum(i for i in range(top + 1)) ** 2
    return sq_sum - sum_sq


if __name__ == '__main__':
    end = int(argv[1])
    print(cheat(end))
