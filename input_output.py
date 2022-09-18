# Read in a string

my_str = input()
print(my_str)


n = int(input())
print(n, end=" test")

#%%
import sys

nums = list(map(int, input().split()))
nums = list(map(int, sys.stdin.readline().split()))

#%%
import sys

a, b, c = map(int, input().split())
a, b, c = map(int, sys.stdin.readline().split())

#%%
fin = open("problemname.in", "r")
fout = open("problemname.out", "w")
a,b = map(int,(fin.readline().split(' ')))

fout.write(f'{res}') 


line1 = fin.readline()
line_list = []
for line in fin.readlines():
	pass  

output_text = '69'
fout.write(output_text) 