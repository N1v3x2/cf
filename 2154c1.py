from collections import defaultdict
from math import isqrt
import sys

input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

def sieve(n: int) -> tuple[list[int], set[int]]:
    """Get list of all primes <= n"""
    is_prime = [True] * (n + 1)

    for i in range(2, n + 1):
        if not is_prime[i]:
            continue
        for j in range(i**2, n + 1, i):
            is_prime[j] = False

    primes, prime_set = [], set()
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            prime_set.add(i)

    return primes, prime_set

N = 2 * int(1e5)
primes, prime_set = sieve(N)

def factors(x: int) -> set[int]:
    """Get prime factors of x"""
    if x in prime_set:
        return {x}
    facts = set()

    # Optimization: iterate through primes from [2, isqrt(x)]
    # rather than all numbers
    root = isqrt(x)
    for y in primes:
        if y > x or y > root:
            break
        if x % y == 0:
            facts.add(y)
            while x % y == 0:
                x //= y
            # TODO: need to add potential factor here

    return facts

def solve():
    _, A, _, = II(), LII(), LII()
    all_facts = [factors(a) for a in A]
    all_facts2 = [factors(a + 1) for a in A]
    fact_cnt, fact_cnt2 = defaultdict(int), defaultdict(int)

    for facts in all_facts:
        for fact in facts:
            fact_cnt[fact] += 1
    for facts in all_facts2:
        for fact in facts:
            fact_cnt2[fact] += 1

    best = 2
    for i, facts in enumerate(all_facts):
        if A[i] == 1:
            if 2 in fact_cnt:
                best = 1
        else:
            for fact in facts:
                # Check whether gcd(ai, aj) > 1 already
                if fact_cnt[fact] > 1:
                    return 0

                # Check whether gcd(ai, aj) > 1 if
                # we add 1 to only a single ai
                if (fact not in all_facts2[i] and fact_cnt2[fact] > 0) \
                        or (fact in all_facts[i] and fact_cnt2[fact] > 1):
                    best = 1
    return best

def main():
    T = II()
    for _ in range(T):
        ans = solve()
        print(ans)
main()
