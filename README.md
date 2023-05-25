# Primality Testing Algorithms
This repository contains the implementation of four different primality testing algorithms:

* Fermat's Primality Test
* Miller-Rabin Primality Test
* Agrawal-Kayal-Saxena (AKS) Primality Test
* Trial Division

The repository includes a Python implementation of each algorithm and a data generator for generating test numbers of varying sizes for evaluating the performance of each algorithm.

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
Trial Division is a deterministic primality test that assesses a number's primality by dividing it by all integers up to its square root. A number is prime if none of these integers divide it evenly, i.e., without leaving a remainder. For example, determining whether 71 is prime is divided by integers up to $\sqrt{8} \approx (8.43)$. As none of these divisions yield a zero remainder, 71 is deemed prime.

### **Fermat's Primality Test**
Fermat's test, a probabilistic primality algorithm, utilizes Fermat's Little Theorem. The algorithm iterates $k$ times and randomly selects an integer $a$ between 2 and $p-1$ in each iteration. If for all iterations, the congruence $a^{p-1} \equiv 1 \pmod{p}$ holds, then $p$ is likely prime. Any violation of the congruence identifies $p$ as composite, with $a$ serving as Fermat's witness to compositeness. The time complexity of this algorithm is $O(k \hspace{0.25em} \log n)$, where $n$ is the candidate prime and $k$ is the number of test iterations.

### **Miller-Rabin Primality Test**
The Miller-Rabin test is a probabilistic primality algorithm with time complexity $O(k \hspace{0.25em} log^{3(n)})$, where $n$ is the candidate prime and $k$ the number of test iterations. Building upon Fermat's test and modulo congruences, it uses a system of congruences to establish "witnesses," values indicating compositeness. An odd prime lacks Miller-Rabin witnesses; thus, if $n$ possesses a witness, it is composite. This method is often favored, with 75% of numbers from 2 to $n-1$ acting as witnesses for odd composites.

### **Agrawal-Kayal-Saxena (AKS) Primality Test**
The AKS algorithm, a deterministic polynomial-time primality test, operates on the theorem stating that an integer $n > 2$ is prime if the polynomial congruence relation $(X + a)^ n = (X^n + a) \hspace{0.1cm} (mod \hspace{0.1cm} n)$ holds for some $a$ coprime to $n$.

The test first ensures $n \geq 1$, then checks if $n$ is a perfect power (thus non-prime). It then finds the smallest $r$ such that $n \bmod r$ exceeds the square root of $r$'s most significant prime factor. After setting these bounds, the test examines $n$'s greatest common divisor and checks if the polynomial congruence holds for integers $1$ to $\sqrt{r}+1$.

If satisfied, $n$ is prime. Its time complexity is $O(log^6 n)$. While noted for theoretical importance as the first deterministic primality test, AKS is not the most efficient, and probabilistic tests, like Miller-Rabin, can often prove superior.

## Performance Evaluation
This table presents the execution times (in seconds) of four primality testing algorithms - Fermat's, Miller-Rabin, AKS, and Trial Division–for numbers of varying digit lengths.

In general, as the digit length of the tested number increases, the execution time of all algorithms also increases. For smaller digit lengths (1 to 17 digits), all algorithms are feasible with relatively low execution times.

Fermat's test and Miller-Rabin's test show similar time complexity, exhibiting relatively consistent and manageable increases in execution time, even as the digit length increases to 300. These algorithms remain practical for large numbers.

The AKS test also shows a steady increase in time with increased digit length. However, its execution time rises more sharply than Fermat's and the Miller-Rabin test, especially for numbers with higher digit lengths, indicating it might be less efficient for more significant numbers.

Trial Division, on the other hand, becomes impractical for larger numbers. For numbers up to 18 digits, the execution time increases faster than the other algorithms. Beyond 18 digits, the execution time becomes infeasibly high (represented as 'inf'), suggesting that the algorithm cannot handle numbers of this magnitude effectively.

In summary, for testing the primality of large numbers, Fermat's test and the Miller-Rabin test offer the most efficient performance. In contrast, the AKS test could be more efficient, and Trial Division could be more practical.

Digits | Fermat | Miller-Rabin | AKS | Trial Division
:---- |:--- |:--- |:--- |:---
1 | 0.000016 | 0.000004 | 0.000008 | 0.000002       
2 | 0.000007 | 0.000003 | 0.000011 | 0.000001       
3 | 0.000006 | 0.000004 | 0.000009 | 0.000001       
4 | 0.000003 | 0.000004 | 0.000011 | 0.000002       
5 | 0.000003 | 0.000003 | 0.000017 | 0.000005       
6 | 0.000004 | 0.000003 | 0.000022 | 0.000018       
7 | 0.000004 | 0.000004 | 0.000030 | 0.000061       
8 | 0.000005 | 0.000004 | 0.000038 | 0.001114       
9 | 0.000005 | 0.000004 | 0.000043 | 0.000515       
10 | 0.000734 | 0.000015 | 0.000065 | 0.009271       
11 | 0.000019 | 0.000014 | 0.000079 | 0.014000       
12 | 0.000015 | 0.000015 | 0.000082 | 0.054911       
13 | 0.000016 | 0.000014 | 0.000101 | 0.106705       
14 | 0.000026 | 0.000020 | 0.000123 | 0.145269       
15 | 0.000028 | 0.000016 | 0.000141 | 0.851116       
16 | 0.000033 | 0.000023 | 0.000185 | 1.760991       
17 | 0.000033 | 0.000022 | 0.000178 | 4.813058       
18 | 0.000036 | 0.000023 | 0.000236 | 20.029892      
19 | 0.000042 | 0.000035 | 0.000237 | inf            
20 | 0.000026 | 0.000026 | 0.000222 | inf            
21 | 0.000029 | 0.000029 | 0.000247 | inf            
22 | 0.000029 | 0.000028 | 0.000256 | inf            
23 | 0.000030 | 0.000029 | 0.000290 | inf            
24 | 0.000036 | 0.000032 | 0.000309 | inf            
25 | 0.000029 | 0.000029 | 0.000318 | inf            
50 | 0.000143 | 0.000128 | 0.001368 | inf            
75 | 0.000380 | 0.000375 | 0.003230 | inf            
100 | 0.000831 | 0.000821 | 0.005820 | inf            
150 | 0.002301 | 0.002335 | 0.013559 | inf            
200 | 0.004950 | 0.004996 | 0.025594 | inf            
250 | 0.007799 | 0.007960 | 0.044614 | inf            
300 | 0.013813 | 0.013682 | 0.057153 | inf            

![](./docs/primality_testing_performance.png)