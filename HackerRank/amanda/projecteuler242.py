from math import log
import itertools

m, r, n, k, M = input().split()
vec =[]
n = int(n)
m = int(m)
r = int(r)
k = int(k)
M = int(M)

for i in range(1, n+1):
    vec.append(i)

w= input('waiting')
s = ((1 + n)*n)/2

somas = []
i = r
while(i < s):
    somas.append(i)
    i = i + m
#print(somas)
w= input('waiting')
subc = list(itertools.combinations(vec, int(k)))
#print(subc)
#print(sum(subc[1]))
x = 0

for i in range(len(subc)):
    if sum(subc[i]) in somas:
        x += 1
resultado = (m*x)%M

print(resultado)

