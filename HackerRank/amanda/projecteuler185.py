import math

n = int(input())
m = []
mc = []
chars = 12
certas =[]
for i in range(chars):
    m.append(['1','2','3','4','5','6','7','8','9','0'])
    mc.append(['0','0','0','0','0','0','0','0','0','0'])


for i in range(n):
    a = str(input())
    a = a.split(' ')
    num = a[0]
    c = int(a[1])
    2
    if c == 0:
        for j in range(chars):
            if num[j] in m[j]:
                m[j].remove(num[j])
    else:
        certas.append(num)
        for j in range(chars):
            if num[j] in m[j]:
                mc[j][int(num[j])-1] = int(mc[j][int(num[j])-1]) + int(num[j])
##    for j in range(len(certas)):
##        if num[j] in
print(m)
print(mc)
print(certas)