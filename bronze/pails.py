import sys
sys.stdin = open("pails.in", "r")
sys.stdout = open("pails.out", "w")

x,y,m = map(int,input().split())
res = 0
for i in range(m//x+1+(m%x==0)):
    res = max(res,i*x+y*((m-i*x)//y))
print(res)
