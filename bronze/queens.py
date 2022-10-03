reserved = set()
for i in range(8):
    for j,s in enumerate(input()):
        if s == '*': reserved.add((i,j))
board = [None]*8
global res
res = 0
def is_safe(i,j):
    if i in board: return False
    for jj,ii in enumerate(board):
        if ii != None and abs(i-ii) == abs(j-jj): return False
    return True

def backtrack(j):
    global res
    if j == 8:
        res += 1
        return
    for i in range(8):
        if is_safe(i,j) and (i,j) not in reserved:
            board[j] = i
            backtrack(j+1)
            board[j] = None
backtrack(0)
print(res)
