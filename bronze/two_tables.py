
def solve(W,H,r1,w2,h2):
    res = float('inf')
    w1, h1 = r1[2]-r1[0],r1[3]-r1[1]
    top_place = H-h2
    bottom_place = h2
    left_place = w2
    right_place = W-w2
    left_move = max(left_place-r1[0],0) 
    right_move = max(r1[2]-right_place,0) 
    top_move = max(r1[3]-top_place,0) 
    bottom_move = max(bottom_place-r1[1],0)
    if w1+w2 > W:
        left_move = float('inf')
        right_move = float('inf')
    if h1+h2 > H:
        top_move = float('inf')
        bottom_move = float('inf')
    res = min(left_move,right_move,top_move,bottom_move)
    return res if res != float('inf') else -1

t = int(input())
for i in range(t):
    W, H = map(int, input().split())
    r1 = tuple(map(int, input().split()))
    w2, h2 = map(int, input().split())
    print(solve(W, H, r1, w2, h2))
