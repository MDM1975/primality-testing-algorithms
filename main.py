import time
from code.primes import primes
from code.trial_division import trial_division
from code.fermat import fermat
from code.miller_rabin import miller_rabin
from code.aks import aks

def speed_test():
    print('{:<10s} {:<5s} {:<5s} {:<5s} {:<5s}'.format('digits', 'fermat', 'rabin_miller', 'aks', 'trial_division'))
    for index, prime in enumerate(primes):
        fermat_start = time.perf_counter()
        fermat(prime)
        fermat_end = time.perf_counter()

        miller_rabin_start = time.perf_counter()
        miller_rabin(prime)
        miller_rabin_end = time.perf_counter()

        aks_start = time.perf_counter()
        aks(prime)
        aks_end = time.perf_counter()

        trial_division_start = time.perf_counter()
        """the trial division algorithm is too slow to run on large primes"""
        trial_division(prime) if index < 10 else None
        trial_division_end = time.perf_counter()

        print('{:<10d} {:<5f} {:<5f} {:<5f} {:<5f}'.format(
            len(str(prime)), 
            fermat_end - fermat_start, 
            miller_rabin_end - miller_rabin_start, 
            aks_end - aks_start, 
            trial_division_end - trial_division_start
        ))

speed_test()