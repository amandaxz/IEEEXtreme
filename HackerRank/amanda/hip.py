
board = []
playerPos = []
enemyPos = []
availablePos = []

def distance(pos):
    

player = input()
for i in range(9):
    board.append([])
    row = input()
    for j in range(9):
        char = row[j]
        if char == '-':
            availablePos.append([i, j])
        if char == 'b' or char == 'r':
            if char == player:
                playerPos.append([i, j])
            else:
                enemyPos.append([i, j])
        board[i].append(char)

print(board)
print('playerPos: ' + str(playerPos))
print('enemyPos: ' + str(enemyPos))
print('availablePos: ' + str(availablePos))