import math


def is_prime(candidate: int) -> bool:
    factor = 2
    candidate_sqrt = math.sqrt(candidate)
    while factor <= candidate_sqrt:
        if candidate % factor == 0:
            return False
        factor += 1
    return True