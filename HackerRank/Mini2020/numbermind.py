def split(numbers):
    return  [char for char in numbers]

n = int(input())

sequence = [[0]*2]*n
char = '0123456789'
key = [0] * 12

for i in range (n):
    a, b = input().split()
    a = split(a)
    sequence[i] = [a, b]

# Testa todos os errados
for j in range(12):
    for i in range(n):
        if sequence[i][1] == '0':
            c = sequence[i][0][j]
            char = char.replace(c, '')
    # key += char
    key[j] = char
    char = '0123456789'

# print(key)

# Compara as sequências de dígito 1 com as possibilidades
for i in range(n):
    if sequence[i][1] == '1':
        for j in range(12):
            t = len(key[j])
            igual = 0
            for l in range(t):
                if sequence[i][0][j] == key[j][l]:
                    igual = 1
            if not igual:
                sequence[i][0][j] = ' '

# # Imprime novas sequências substituídas

# for i in range(n):
#     if sequence[i][1] == '1':
#         print(sequence[i])

# Confere as linhas que tem apenas um dígito certo

for i in range(n):
    if sequence[i][1] == '1':
        soma = 0
        pos = 0 
        for j in range(12):
            if sequence[i][0][j] != ' ':
                soma += 1
                pos = j
        if soma == 1:
            key[pos] = sequence[i][0][pos]
            sequence[i][1] = '0'

# Imprime novas sequências com linhas limpas

# for i in range(n):
#     if sequence[i][1] == '1':
#         print(sequence[i])

# print(key)

# Limpa as opções das linhas que tem uma opção certa

for i in range(12):
    t = len(key[i])
    if t == 1:
        for j in range(n):
            if sequence[j][1] == '0':
                if sequence[j][0][i] == key[i]:
                    sequence[j][0][i] = 0
                    for k in range(12):
                        if sequence[j][0][k] != ' ':
                            print("entrou")
                            char = str(sequence[j][0][k])
                            opc = key[k]
                            opc = opc.replace(char, '')
                            key[k] = opc
                            sequence[j][0][k] = ' '
                else:
                    sequence[j][0][i] = ' '

# Corrigi as linhas que já tem acertos

for i in range(n):
    if sequence[i][1] == '1':
        print(sequence[i])

print(key)
