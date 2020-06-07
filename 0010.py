from sys import argv

from primes import is_prime


def sum_of_primes(goal_val: int) -> int:
    result = 2
    for candidate in range(3, goal_val, 2):
        if is_prime(candidate):
            result += candidate
    return result


if __name__ == '__main__':
    goal = int(argv[1])
    print(f"Sum of primes up to {goal} is {sum_of_primes(goal)}")
