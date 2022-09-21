N = int(input())
rounds = []
for _ in range(N):
    rounds.append(tuple(map(int,input().split())))

res,max_points = '',0
game = [0,1,2]
counter = [0]*3
for p1, p2, g in rounds:
    game[p1-1],game[p2-1] = game[p2-1],game[p1-1]
    counter[game[g-1]] += 1
print(max(counter))