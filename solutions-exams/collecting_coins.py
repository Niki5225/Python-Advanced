from math import floor


def get_position(command, player_r, player_c):
    if command == "right":
        if player_c + 1 >= cols:
            return player_r, 0
        else:
            return player_r, player_c + 1
    elif command == "left":
        if player_c - 1 < 0:
            return player_r, cols - 1
        else:
            return player_r, player_c - 1
    elif command == "up":
        if player_r - 1 < 0:
            return rows - 1, player_c
        else:
            return player_r - 1, player_c
    elif command == "down":
        if player_r + 1 >= rows:
            return 0, player_c
        else:
            return player_r + 1, player_c


path = []
credits = 0

number = int(input())
rows, cols = number, number
matrix = []

for r in range(rows):
    matrix.append(input().split())

player_r = 0
player_c = 0

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == "P":
            player_r = r
            player_c = c

won = False
while True:
    path.append([player_r, player_c])
    if credits >= 100:
        won = True
        break
    command = input()
    player_r, player_c = get_position(command, player_r, player_c)
    if matrix[player_r][player_c].isdigit():
        credits += int(matrix[player_r][player_c])
        matrix[player_r][player_c] = ''
    elif matrix[player_r][player_c] == "X":
        path.append([player_r, player_c])
        credits /= 2
        break

if won:
    print(f"You won! You've collected {credits} coins.")
else:
    print(f"Game over! You've collected {floor(credits)} coins.")
print("Your path:")
for el in path:
    print(el)
