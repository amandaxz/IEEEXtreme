# Correta
# Mas está desnecessariamente longa

def four_xtremes(a, b, c, d):
    max = 0
    min = 0
    if a > b:
        if a > c:
            if a > d:
                max = a
            else:
                max = d
        else:
            if c > d:
                max = c
            else:
                max = d
    else:
        if b > c:
            if b > d:
                max = b
            else:
                max = d
        else:
            if c > d:
                max = c
            else:
                max = d
                
    if a < b:
        if a < c:
            if a < d:
                min = a
            else:
                min = d
        else:
            if c < d:
                min = c
            else:
                min = d
    else:
        if b < c:
            if b < d:
                min = b
            else:
                min = d
        else:
            if c < d:
                min = c
            else:
                min = d
                
    max_diff = max - min
    return(max_diff)
    
a, b, c, d = map(int, input().split(' '))
max_diff = four_xtremes(a, b, c, d)
print(max_diff)
