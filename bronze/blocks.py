import sys
sys.stdin = open("censor.in", "r")
sys.stdout = open("censor.out", "w")

s = input()
t = input()
def rec_delete(s,t):
    if t not in s: return s
    i = s.index(t)
    return delete(s[:i]+s[i+len(t):],t)
# print(rec_delete(s,t))

def delete(s,t):
    word = ''
    for ch in s:
        word += ch
        if word[-len(t):] == t: word = word[:-len(t)] 
    return word
print(delete(s,t))