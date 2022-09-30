import sys
sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")

s = input()
first,second = {},{}
for i in range(len(s)):
    if s[i] not in first:
        first[s[i]] = i
    second[s[i]] = i

print(sum(first[c1] <  first[c2] < second[c1] < second[c2] for c1 in first for c2 in first))