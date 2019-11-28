import sys
from typing import Tuple, Optional


def max_palindrome(num_digits: int) -> int:
    start = max_product(num_digits)
    stop = min_product(num_digits)
    for i in range(start, stop - 1, -1):
        if is_palindrome(str(i)):
            factors = max_factors(i, num_digits)
            if factors and all([len(str(x)) == num_digits for x in factors]):
                return i


def is_palindrome(word: str) -> bool:
    head = 0
    tail = len(word) - 1
    while head < tail:
        if word[head] != word[tail]:
            return False
        head += 1
        tail -= 1
    return True


def max_product(num_digits: int) -> int:
    max_factor = 10 ** num_digits - 1
    return max_factor * max_factor


def min_product(num_digits: int) -> int:
    min_factor = 10 ** (num_digits - 1)
    return min_factor * min_factor


def max_factors(num: int, num_digits: int) -> Optional[Tuple[int, int]]:
    sqrt = int(num ** .5)
    stop = 10 ** (num_digits - 1) - 1
    for i in range(sqrt, stop, -1):
        div, rem = divmod(num, i)
        if not rem and div > stop and i > stop:
            return i, div
    return None


if __name__ == '__main__':
    factor_length = int(sys.argv[1])
    print(max_product(factor_length))

    print(max_factors(9009, 2))

    print(is_palindrome("123211"))

    print(max_palindrome(3))
