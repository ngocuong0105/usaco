fin = open("square.in", "r")
fout = open("square.out", "w")
ax1,ay1,ax2,ay2 = map(int,(fin.readline().split(' ')))
bx1,by1,bx2,by2 = map(int,(fin.readline().split(' ')))

w = max(bx2,ax2) - min(bx1,ax1)
h = max(by2,ay2) - min(by1,ay1)
res = max(w,h)**2
fout.write(f'{res}') 