#https://codeforces.com/problemset/problem/1472/E

def solve(n,people):
    mp,stack = {},[]
    people.sort(key = lambda x: (-x[1],x[2]))
    for i,h,w in people:
        while stack and stack[-1][2] > w:
            mp[stack.pop()[0]] = str(i)
        stack.append((i,h,w))
    stack = []
    lying = [(i,w,h) for i,w,h in people]
    lying.sort(key = lambda x: (-x[1],x[2]))
    for i,h,w in people:
        while stack and stack[-1][2] > h:
            mp[stack.pop()[0]] = str(i)
        stack.append((i,h,w))
    return ' '.join(mp.get(i+1,str(-1)) for i in range(n))

T = int(input())
for _ in range(T):
    n = int(input())
    people = [[i+1] + list(map(int,input().split())) for i in range(n)]
    print(solve(n,people))