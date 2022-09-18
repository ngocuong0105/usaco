fin = open("paint.in", "r")
fout = open("paint.out", "w")
ax1,ay1, ax2,ay2 = map(int,(fin.readline().split(' ')))
bx1,by1, bx2,by2 = map(int,(fin.readline().split(' ')))
cx1,cy1, cx2,cy2 = map(int,(fin.readline().split(' ')))

def area(a,b,c,d):
    return (d-b)*(c-a)

def overlap(ax1,ay1, ax2,ay2,cx1,cy1, cx2,cy2):
    h = max(0, min(ay2,cy2) - max(ay1,cy1))
    w = max(0, min(ax2,cx2) - max(ax1,cx1))
    return h*w

res = area(ax1,ay1, ax2,ay2) + area(bx1,by1, bx2,by2) - overlap(ax1,ay1, ax2,ay2,cx1,cy1, cx2,cy2 ) - overlap(bx1,by1, bx2,by2,cx1,cy1, cx2,cy2 )

fout.write(res)

#%%
import sys

class Rect:
	def __init__(self):
		self.x1, self.y1, self.x2, self.y2 = map(int, input().split())

	def area(self):
		return (self.y2 - self.y1) * (self.x2 - self.x1)

def intersect(p, q):
	x_overlap = max(0, min(p.x2, q.x2) - max(p.x1, q.x1))
	y_overlap = max(0, min(p.y2, q.y2) - max(p.y1, q.y1))
	return x_overlap * y_overlap

sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

rects = []
for _ in range(3):
	rects.append(Rect())

print(rects[0].area() + rects[1].area() - intersect(rects[0], rects[2]) - intersect(rects[1], rects[2]))