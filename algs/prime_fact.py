#!/usr/bin/env pypy3
from functools import cache
from math import isqrt
from sieve import sieve

N = 2 * int(1e5)
primes = sieve(N)

@cache
def prime_factorization(n: int) -> set[int]:
    if n in primes:
        return {n}
    factors = set()
    root = isqrt(n)
    m = n
    for prime in primes:
        if prime > root:
            break
        if m % prime == 0:
            factors.add(prime)
            while m % prime == 0:
                m //= prime
    if m > 1:
        factors.add(m)
    return factors

if __name__ == '__main__':
    n = int(input("n = "))
    factors = prime_factorization(n)
    print(factors)
