#http://www.usaco.org/index.php?page=viewproblem2&cpid=571
from typing import Any
from utils import submit
from sortedcontainers import SortedList

def solve(inp) -> Any:
    N, cards = inp
    s = set(cards)
    mine = SortedList([num for num in range(1,2*N+1) if num not in s])
    res = 0
    for j in range(N):
        idx = mine.bisect_left(cards[j])
        if idx < len(mine):
            res += 1
            mine.remove(mine[idx])
    return res


def solve(inp) -> Any:
    N, cards = inp
    cards.sort()
    s = set(cards)
    mine = sorted([num for num in range(1,2*N+1) if num not in s])
    res,j = 0,0
    for i in range(N):
        if mine[i] > cards[j]:
            res += 1
            j += 1
    return res

def read_input() -> tuple:
    N = int(input())
    cards = [int(input()) for _ in range(N)]
    return N, cards

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
