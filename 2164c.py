import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

def solve():
    _, a, b, c = (LII() for _ in range(4))
    a.sort()
    monsters = list(sorted(zip(b, c), key=lambda x: (x[0], -x[1])))
    swords_left, monsters_left, res = [], [], 0
    j = 0

    for x in a:
        sword = x
        while j < len(monsters) and sword >= monsters[j][0]:
            bi, ci = monsters[j]
            sword = max(sword, ci)
            if ci > 0:
                # If we can keep our sword or get a better one, just kill the monster
                res += 1
            else:
                # If we lose our sword by killing the monster, save it for later
                heapq.heappush(monsters_left, -bi)
            j += 1
        # Sword has one use left; push onto max-heap
        heapq.heappush(swords_left, -sword)

    while monsters_left and swords_left:
        monster = -monsters_left[0]
        sword = -swords_left[0]
        if sword >= monster:
            heapq.heappop(swords_left)
            heapq.heappop(monsters_left)
            res += 1
        else:
            heapq.heappop(monsters_left)

    return res

output = []
T = II()
for _ in range(T):
    ans = solve()
    output.append(ans)
print(*output, sep='\n')
