# Primality Testing Algorithms
This repository contains the implementation of four different primality testing algorithms:

* Fermat's Primality Test
* Miller-Rabin Primality Test
* Agrawal-Kayal-Saxena (AKS) Primality Test
* Trial Division

The repository includes a Python implementation of each algorithm, as well as a data generator for generating test numbers of varying sizes, and a test suite for evaluating the performance of each algorithm.

## Repository Structure
```zsh
├── README.md
├── code
│   ├── aks.py
│   ├── fermat.py
│   ├── miller_rabin.py
│   ├── primes.py
│   └── trial_division.py
├── docs
│   ├── Exploring the Efficiency and Accuracy of Primality Testing Techniques.pdf
│   └── primality-testing-performance.png
└── main.py
```

## Overview of Algorithms
### **Trial Division**
Trial division is a deterministic algorithm that tests whether a given number is prime or composite by dividing the number by integers up to its square root.

This algorithm initiates by dividing the number by integers, starting with two and continuing until the square root of the number is reached. If any of these integers divide the number with a remainder of 0, the number is deemed composite and not prime.

For instance, to confirm whether 71 is prime, the algorithm divides 71 by integers up to $\sqrt{8} \approxeq (8.43)$. The algorithm divides 71 by 2, 3, 4, 5, 6, 7, and 8, as illustrated below:

* $71 \div 2$ = 35 $\Rightarrow$ ***remainder 1***
* $71 \div 3$ = 23 $\Rightarrow$ ***remainder 2***
* $71 \div 4$ = 17 $\Rightarrow$ ***remainder 3***
* $71 \div 5$ = 14 $\Rightarrow$ ***remainder 1***
* $71 \div 6$ = 11 $\Rightarrow$ ***remainder 5***
* $71 \div 7$ = 10 $\Rightarrow$ ***remainder 1***
* $71 \div 8$ = 8 $\Rightarrow$ ***remainder 7***

### **Fermat's Primality Test**
Fermat's test is a probabilistic algorithm for determining whether a given number is prime based on Fermat's Little Theorem. The theorem states that for any natural number $a$ and prime $p$, $a^{p-1} \equiv 1 \pmod{p}$. Fermat's test randomly selects an integer $a$ between 2 and $p-1$, where $p$ is the number tested for primality. The algorithm consists of two steps:

* **1.** Randomly select a number $a$ for which $1 < a < p$. 
* **2.** Test if the congruence $a^{p-1} \equiv 1 \pmod{p}$ is satisfied.

If the congruence $a^{p-1} \equiv 1 \pmod{p}$ is satisfied, then $p$ may or may not be a prime number. If the congruence is not satisfied, the number $p$ is composite, and $a$ is called Fermat's witness for the compositeness of $p$. The algorithm repeats this process $k$ times, where $k$ is the number of iterations enforced at runtime. If the algorithm returns true for all iterations, $p$ is considered prime. If the algorithm returns false for any iteration, then $p$ is composite.

### **Miller-Rabin Primality Test**
The Miller-Rabin test is a well-known probabilistic algorithm that efficiently determines the likelihood of a given number being prime without providing absolute certainty. It has become the de facto probabilistic primality test, with more than 75\% of numbers from 2 to ${n-1}$ serving as witnesses in the Miller–Rabin test for an odd composite $n>1$. The time complexity of the Rabin-Miller primality test is $O(k \hspace{0.25em} log^{3(n)})$, where $n$ represents the candidate prime number and $k$ is the count of test iterations.

Expanding on the Fermat test, which leverages congruence modulo prime numbers and Fermat's Little Theorem, the Miller-Rabin test employs a similar concept but incorporates a system of congruences. In this context, a "witness" denotes a value that signifies the tested number is composite. An odd prime number does not possess any Miller–Rabin witnesses; therefore, if n has a Miller–Rabin witness, it must be composite.

### **Agrawal-Kayal-Saxena (AKS) Primality Test**
The AKS algorithm is a deterministic primality algorithm that determines whether a given number is prime in polynomial time. The AKS primality test is based on the primality characterization theorem, which states that an integer $n$ greater than 2 is prime if and only if the polynomial congruence relation $(X + a)^ n = (X^n + a) \hspace{0.1cm} (mod \hspace{0.1cm} n)$, holds for some coprime to $n$. 

The algorithm first checks the input number to determine if it equals or exceeds 1. It then determines if the input number is a perfect power, in which case it would not be prime. The algorithm then determines the bounds for checking the primality condition by finding the smallest value of $r$, such that $n$ modulo $r$ is greater than the square root of the most significant prime factor of $r$. With the boundary for the primality check set, the algorithm then determines if the input number has the greatest common denominator. The last step is determining if the polynomial convergence equation holds for all integer values between 1 and the square root of $r+1$. 

If the equation holds, the input value, $n$, is a prime number. The time complexity of the AKS algorithm is $O(log^6 n)$, where $n$ is the number being tested for primality. While the AKS algorithm is noted for its theoretical importance for being the first deterministic primality test, AKS is by no means the most efficient algorithm to determine primality. While the algorithm can efficiently test more significant prime numbers, other probabilistic algorithms, such as the Miller-Rabin test mentioned earlier.

## Performance Evaluation
The following table summarizes the performance of each algorithm for testing the primality of 100 randomly generated numbers of varying sizes. The table includes the average time to test each number, the average number of iterations required to determine primality, and the number of numbers that were incorrectly identified as prime or composite.

Digits | Fermat | Miller-Rabin | AKS | Trial Division 
------|-----------|-----------------|-----|---------------
1 | 0.000011 | 0.000003 | 0.000008 | 0.000001       
2 | 0.000003 | 0.000001 | 0.000010 | 0.000003       
3 | 0.000003 | 0.000002 | 0.000009 | 0.000001       
4 | 0.000002 | 0.000005 | 0.000012 | 0.000003       
5 | 0.000002 | 0.000002 | 0.000017 | 0.000004       
6 | 0.000001 | 0.000002 | 0.000026 | 0.000019       
7 | 0.000002 | 0.000002 | 0.000031 | 0.000063       
8 | 0.000002 | 0.000002 | 0.000038 | 0.000261       
9 | 0.000007 | 0.000004 | 0.000054 | 0.000511       
10 | 0.000008 | 0.000006 | 0.000064 | 0.002767       
11 | 0.000004 | 0.000005 | 0.000069 | inf            
12 | 0.000006 | 0.000006 | 0.000080 | inf            
13 | 0.000005 | 0.000006 | 0.000095 | inf            
14 | 0.000005 | 0.000006 | 0.000104 | inf            
15 | 0.000006 | 0.000007 | 0.000129 | inf            
16 | 0.000007 | 0.000007 | 0.000144 | inf            
17 | 0.000007 | 0.000007 | 0.000157 | inf            
18 | 0.000007 | 0.000007 | 0.000187 | inf            
19 | 0.000013 | 0.000011 | 0.000207 | inf            
20 | 0.000012 | 0.000009 | 0.000233 | inf            
21 | 0.000011 | 0.000011 | 0.000257 | inf            
22 | 0.000011 | 0.000011 | 0.000279 | inf            
23 | 0.000011 | 0.000012 | 0.000308 | inf            
24 | 0.000013 | 0.000012 | 0.000318 | inf            
25 | 0.000011 | 0.000011 | 0.000333 | inf            
50 | 0.000049 | 0.000046 | 0.001479 | inf            
75 | 0.000136 | 0.000135 | 0.003393 | inf            
100 | 0.000289 | 0.000282 | 0.005742 | inf            
150 | 0.000756 | 0.000748 | 0.013490 | inf            
200 | 0.001611 | 0.001608 | 0.024685 | inf            
250 | 0.002562 | 0.002563 | 0.039304 | inf            
300 | 0.004516 | 0.004416 | 0.067171 | inf

![](./docs/primality-testing-performance.png)