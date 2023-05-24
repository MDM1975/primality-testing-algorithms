import random


def fermat(p, k=1):
    if p <= 1 or p % 2 == 0:
        return False

    if p == 2 or p == 3:
        return True

    if p % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, p-1)
        if pow(a, p-1, p) != 1:
            return False

    return True
