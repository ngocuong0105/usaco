from itertools import permutations

def generate_eval(exp: str):
    if exp.isnumeric(): return [eval(exp)]
    res = []
    for i in range(len(exp)):
        if exp[i] in '+-*/':
            for v1 in generate_eval(exp[:i]):
                for v2 in generate_eval(exp[i+1:]):
                    res.append(eval(str(v1)+exp[i]+str(v2)))
    return res
def solve(cards):
    res = 0
    for c1,c2,c3,c4 in permutations(cards,4):
        for s1,s2,s3 in permutations('+-*/',3):
            exp = c1+s2+c2+s2+c3+s3+c4
            for val in generate_eval(exp):
                if val <= 24: res = max(val,res)
    return res