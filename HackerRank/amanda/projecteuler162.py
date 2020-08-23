import itertools
n = int(input())

v = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
#subc = list(itertools.combinations(v, int(n)))
subc = list(itertools.product(v,v, repeat=n))
print(len(subc))
print(subc)