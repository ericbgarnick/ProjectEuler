import sys


PRIMES = {}


def largest_prime_factor(query: int) -> int:
    sqrt = int(query ** .5)
    result = 1
    for factor in range(2, sqrt + 1):
        div, rem = divmod(query, factor)
        if not rem :
            if is_prime(div):
                return div
            elif is_prime(factor):
                result = max(result, factor)
    return result


def is_prime(candidate: int) -> bool:
    try:
        return PRIMES[candidate]
    except KeyError:
        sqrt = int(candidate ** .5)
        for factor in range(2, sqrt + 1):
            if not candidate % factor:
                PRIMES[candidate] = False
                return False
        PRIMES[candidate] = True
        return True


if __name__ == '__main__':
    num = int(sys.argv[1])
    res = largest_prime_factor(num)
    print(f"largest prime factor of {num} is: {res}")
