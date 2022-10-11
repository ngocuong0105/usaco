def transform(cows):
    arr = []
    for i in range(0,len(cows),2):
        if cows[i] == cows[i+1]:
            arr.append('.')
        else:
            arr.append('A' if cows[i] == 'G' else 'B')
    return arr
def compress(arr):
    arr = [arr[i] for i in range(len(arr)) if arr[i] != '.']
    groups,i = [],0
    while  i < len(arr):
        groups.append(arr[i])
        i += 1
        while i < len(arr) and arr[i] == arr[i-1]:
            i += 1
    return groups
def truncate(arr):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == 'A': break
    else:
        i = -1
    return arr[:i+1]
N = int(input())
arr = truncate(compress(transform(input())))
print(len(arr))
