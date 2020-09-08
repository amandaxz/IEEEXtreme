def f(un, b):
    return (2**(b-un*un))*(10**(-9))

u0, b = input().split()
u0, b = float(u0), float(b)

u1 = u0

for i in range (1000):
    u2 = f(u1, b)
    sub = u1
    u1 = u2

sum = sub + u1

print("%.9f" % sum)
