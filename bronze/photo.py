N = int(input())
nums = list(map(int,input().split()))
odd = sum(num%2 for num in nums)
even = sum(num%2==0 for num in nums)
need_even,res = True,0
while True:
    if need_even:
        if even: even -= 1
        elif odd>1: odd -= 2
        else: break
    else:
        if odd: odd -= 1
        else: break
    need_even = 1-need_even
    res += 1
print(res-(odd==1))