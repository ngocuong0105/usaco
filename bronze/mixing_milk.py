c1, m1 = map(int,input().split())
c2, m2 = map(int,input().split())
c3, m3 = map(int,input().split())

milk = [m1,m2,m3]
cap = [c1,c2,c3]

for i in range(100):
    pour_to = (i+1)%3
    pour_from = i%3
    pour = min(milk[pour_from],cap[pour_to]-milk[pour_to])
    milk[pour_from] -= pour
    milk[pour_to] += pour

print(milk)