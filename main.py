import time
# import matplotlib.pyplot as plot
from code.primes import primes
from code.trial_division import trial_division
from code.fermat import fermat
from code.miller_rabin import miller_rabin
from code.aks import aks


def speed_test():
    time_fermat = []
    time_miller_rabin = []
    time_aks = []
    time_trial_division = []

    for prime in primes:
        time_fermat.append(time_execution(fermat, prime))
        time_miller_rabin.append(time_execution(miller_rabin, prime))
        time_aks.append(time_execution(aks, prime))

        if len(str(prime)) <= 10:
            time_trial_division.append(time_execution(trial_division, prime))
        else:
            time_trial_division.append(None)

    print_and_plot_results(
        primes,
        time_fermat,
        time_miller_rabin,
        time_aks,
        time_trial_division
    )


def time_execution(primality_test, prime):
    start_time = time.process_time()
    primality_test(prime)
    end_time = time.process_time()
    return end_time - start_time


def print_and_plot_results(primes, time_fermat, time_rabin_miller, time_aks, time_trial_division):
    digit_lengths = [len(str(p)) for p in primes]

    print('{:<10s} {:<10s} {:<12s} {:<10s} {:<15s}'.format(
        'Digits',
        'Fermat',
        'Miller-Rabin',
        'AKS',
        'Trial Division'
    ))

    for index, _ in enumerate(primes):
        print('{:<10d} {:<10.6f} {:<12.6f} {:<10.6f} {:<15.6f}'.format(
            digit_lengths[index],
            time_fermat[index],
            time_rabin_miller[index],
            time_aks[index],
            time_trial_division[index] if time_trial_division[index]
            else float('inf')
        ))

    # plot.figure(figsize=(10, 6))
    # plot.plot(digit_lengths, time_fermat, label='Fermat')
    # plot.plot(digit_lengths, time_rabin_miller, label='Rabin-Miller')
    # plot.plot(digit_lengths, time_aks, label='AKS')
    # plot.plot(digit_lengths, time_trial_division, label='Trial Division')
    # plot.xlabel('Digits')
    # plot.ylabel('Execution Time (s)')
    # plot.title('Primality Testing Performance')
    # plot.legend()
    # plot.show()


speed_test()
