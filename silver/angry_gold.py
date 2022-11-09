#http://www.usaco.org/index.php?page=viewproblem2&cpid=597
from typing import Any
from sortedcollections import SortedList
from utils import submit

def possible_first(nums,x,radius):
    i = nums.bisect_left(x-radius)
    curr = nums[i]
    radius -= 2
    while curr != nums[0]:
        i = nums.bisect_left(curr-radius)
        nxt = nums[i]
        if nxt >= curr: return False
        curr = nxt
        radius -= 2
    return True

def possible_last(nums,x,radius):
    i = nums.bisect_right(x+radius)-1
    if i == len(nums): return True
    curr = nums[i]
    radius -= 2
    while curr != nums[-1]:
        i = nums.bisect_right(curr+radius)-1
        if i == len(nums): return True
        nxt = nums[i]
        if nxt <= curr: return False
        curr = nxt
        radius -=2
    return True

def blow_all(nums, radius):
    l,r = nums[0]+1,nums[-1]+1
    while l < r:
        m = l+r>>1
        if not possible_first(nums, m, radius):
            r = m
        else:
            l = m+1
    if possible_last(nums, l-1, radius):
        return True
    return False

def solve(inp) -> Any:
    nums = inp
    nums = [2*num for num in nums] # trick to work only with integers
    nums = SortedList(nums)
    l,r = 0, nums[-1]
    while l<r:
        radius = l+r >> 1
        if blow_all(nums, radius):
            r = radius
        else:
            l = radius+1
    return l/2

def read_input() -> tuple:
    N = int(input())
    nums = [ int(input()) for _ in range(N)] 
    return nums

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
