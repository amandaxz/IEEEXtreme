all_primes = []

t = int(input())

sum = 0

for i in range(t):
    n = int(input())
    primer = 0
    if i == 2:
        sum += 1
    elif i % 2 == 1 and i >= 9:
        