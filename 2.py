def fib_sum(stop: int) -> int:
    old = 0
    cur = 1
    total = 0
    while cur <= stop:
        old, cur = cur, old + cur
        if not cur % 2:
            total += cur
    return total


if __name__ == '__main__':
    print(fib_sum(4000000))

