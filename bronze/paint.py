fin = open("paint.in", "r")
fout = open("paint.out", "w")
a,b = map(int,(fin.readline().split(' ')))
c,d = map(int,(fin.readline().split(' ')))
def overlap(a,b,c,d):
    return max(0,min(b,d) - max(a,c))

fout.write(b-a+c-d - overlap(a,b,c,d))