import sys

input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

def solve():
    (n, q), A = LII(), LII()
    A.sort()

    for _ in range(q):
        c = II()

        ans = 0
        for i, a in enumerate(A):
            while a > 0:
                j = c.bit_count() - 1
                if a < 1 << j:
                    # TODO: rework this logic
                    pass

                elif a < 1 << (j + 1):
                    a ^= 1 << j
                    c ^= 1 << j
                else:
                    c = 0
                    break
            if c == 0:
                break
        ans += c
        print(ans)

def main():
    T = II()
    for _ in range(T):
        solve()
main()
