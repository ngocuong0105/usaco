N = int(input())
d = {'Bessie':(0,'Ox')}
zodiac = ['Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat']
for _ in range(N):
    s = list(input().split())
    i = zodiac.index(d[s[-1]][1])
    year = d[s[-1]][0]
    if s[4] == zodiac[i]:
        year += ((s[3] == 'next') - (s[3] == 'previous'))*12
    while s[4] != zodiac[i]:
        i += (s[3] == 'next') - (s[3] == 'previous')
        year += (s[3] == 'next') - (s[3] == 'previous')
        i %= len(zodiac)
    animal = s[4]
    d[s[0]] = (year,animal)
print(abs(d['Elsie'][0]))