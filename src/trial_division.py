import math


def trial_division(n):
    if n <= 1 or n % 2 == 0:
        return False

    if n == 2 or n == 3:
        return True

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
