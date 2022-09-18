fin = open("billboard.in", "r")
fout = open("billboard.out", "w")
ax1,ay1,ax2,ay2 = map(int,(fin.readline().split(' ')))
bx1,by1,bx2,by2 = map(int,(fin.readline().split(' ')))

x_overlap = max(0,min(ax2,bx2) - max(ax1,bx1))
y_overlap = max(0,min(ay2,by2) - max(ay1,by1))

res = (ax2-ax1) * (ay2-ay1)

# and not(ay1<by1 and by2<ay2) and not (ax1<bx1 and bx2<ax2) ## xase when the second rectangle is inside the first and matches perfectly
if (x_overlap==(ax2-ax1) or y_overlap==(ay2-ay1)) and not(ay1<by1 and by2<ay2) and not (ax1<bx1 and bx2<ax2):
    res -= x_overlap*y_overlap

fout.write(f'{res}')
