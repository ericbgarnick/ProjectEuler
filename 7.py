from sys import argv


def nth_prime(n: int) -> int:
    last_val = 1
    while n:
        last_val += 1
        if is_prime(last_val):
            n -= 1
    return last_val


def is_prime(candidate: int) -> bool:
    factor = 2
    while factor ** 2 <= candidate:
        if candidate % factor == 0:
            return False
        factor += 1
    return True


if __name__ == '__main__':
    prime_num = int(argv[1])
    print(f"Prime number {prime_num} is {nth_prime(prime_num)}")
