import math

a = input()
a = a.split(' ')
uo = float(a[0])
b = float(a[1])

for i in range(1, 1000):
    uo = math.floor(2**(b-(uo**2)))*(10**(-9))
uo = uo + math.floor(2**(b-(uo**2)))*(10**(-9))
print(uo)