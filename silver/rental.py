from itertools import accumulate
from typing import Any
from utils import submit

def bs(arr,num):
    l,r = 1,len(arr)
    while l < r:
        m = l + r >> 1
        if arr[m] > num:
            r = m
        else:
            l = m + 1
    return l-1

# optimnized with prefix precalculations
def profit(cum_milk,cum_rent,cum_galoons_sell,cum_prices_sell,prices,for_rent):
    money_from_rent = cum_rent[min(len(cum_rent)-1,for_rent)]
    galoons = cum_milk[min(len(cum_milk)-1,max(0,len(cum_milk)-for_rent-1))]
    i = bs(cum_galoons_sell,galoons)
    rem_gal = galoons - cum_galoons_sell[i]
    money_from_sell = cum_prices_sell[i] + rem_gal* (prices[i][1] if i < len(prices) else 0)
    return money_from_rent + money_from_sell

def solve(inp) -> Any:
    milk, prices, rent = inp
    milk.sort(reverse = True)
    rent.sort(reverse = True)
    prices.sort(key = lambda x: -x[1])
    res = 0
    cum_rent = [0] + list(accumulate(rent))
    cum_milk = [0] + list(accumulate(milk))
    cum_galoons_sell = [0] + list(accumulate([g for g,_ in prices]))
    cum_prices_sell = [0] + list(accumulate([p*g for g,p in prices]))
    for for_rent in range(len(milk),-1,-1): 
        res = max(res,profit(cum_milk,cum_rent,cum_galoons_sell,cum_prices_sell,prices,for_rent))
    return res

def read_input() -> tuple:
    N, M, R = tuple(map(int,input().split()))
    milk = [int(input()) for _ in range(N)]
    prices = [tuple(map(int,input().split())) for _ in range(M)] 
    rent = [int(input()) for _ in range(R)]
    return milk, prices, rent

submit(solve, read_input, test_cases=[])
# #%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
