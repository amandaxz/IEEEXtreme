def cleanzeros(n, key, sequence):
    # Limpa a lista 
    for i in range(n):
        # Confere se o dígito é 0
        print (f'Linha {i}')
        if sequence[i][1] == '0':
            # Confere número a número da sequência, j é a posição
            print(f'Sequência {sequence[i][0]}')
            for j in range(12):
                dig = sequence[i][0][j]
                lenght = len(key[j])
                # Confere a posição da chave
                for k in range(lenght):
                    if (key[j][k] == dig):
                        print(dig)
                        print(key[j])
                        key[j][k].replace(dig, '')
    return key

                

n = int(input())

sequence = [[0]*2]*n
key = ['0123456789'] * 12

for i in range (n):
    a, b = input().split()
    sequence[i] = [a, b]

print(key)
key = cleanzeros(n, key, sequence)
print(key)

