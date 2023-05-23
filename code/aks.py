import math

def aks(n):
    def is_power_of_smaller_prime(n):
        for i in range(2, int(math.log2(n)) + 1):
            if round(n ** (1 / i)) ** i == n:
                return True
        return False

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def find_r(n):
        max_r = int(math.log2(n) ** 2)
        for r in range(2, max_r + 1):
            if n % r == 0:
                return None
            if pow(n, (n - 1) // r, r) != 1:
                return r
        return None

    if n <= 1 or n % 2 == 0:
        return False

    if n == 2 or n == 3:
        return True

    if is_power_of_smaller_prime(n):
        return False

    r = find_r(n)
    if r is None:
        return False

    for a in range(2, r):
        if gcd(a, n) > 1:
            return False

    for a in range(1, int(math.sqrt(r)) + 1):
        if pow(n, a, n) != pow(a, n, n):
            return False

    return True

