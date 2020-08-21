# Incorreta

sum = 0
n = int(input())
k = 0
txt = ""

def myPow(power, num):
    powered = num
    while num > 1:
        powered *= num 
        return powered

def qntpar(s):
    global sum
    if (s%2 == 0):
        sum += 1
        s = s/2
        qntpar(s)    
    else:
        return sum

if n%2 == 1:
    j = int((n-1)/2)
    for i in range (j):
        txt = txt + "y"
    txt = txt + "Y"
    for i in range (j):
        txt = txt + "y"
    print(txt)
else:
    qntpar(n)
    k = sum
    j = int(n*(myPow(2,k)-1)/myPow(2,k))
    for i in range (j):
        txt = txt + "y"
    for i in range (n-j):
        txt = txt + "Y"
    print(txt)


