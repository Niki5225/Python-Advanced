from collections import deque


def get_position(row, col, current_command):
    if current_command == "up":
        if row - 1 < 0:
            return 5, col
        else:
            return row - 1, col
    elif current_command == "down":
        if row + 1 > 5:
            return 0, col
        else:
            return row + 1, col
    elif current_command == "left":
        if col - 1 < 0:
            return row, 5
        else:
            return row, col - 1
    elif current_command == "right":
        if col + 1 > 5:
            return row, 0
        else:
            return row, col + 1


def get_deposit(row, col, matrix):
    if matrix[row][col] == "W":
        deposits["Water"] += 1
        return "Water"
    elif matrix[row][col] == "M":
        deposits["Metal"] += 1
        return "Metal"
    else:
        deposits["Concrete"] += 1
        return "Concrete"


matrix = []
for row in range(6):
    matrix.append(input().split())
commands = deque([x for x in input().split(", ")])

row = 0
col = 0
found = False

for row1 in range(len(matrix)):
    for col1 in range(len(matrix[row])):
        if matrix[row1][col1] == "E":
            row = row1
            col = col1
            found = True
            break
    if found:
        break

broken = False
deposits = {"Water": 0,
            "Metal": 0,
            "Concrete": 0
            }

while commands and not broken:
    current_command = commands.popleft()
    row, col = get_position(row, col, current_command)

    if matrix[row][col] == "W" or matrix[row][col] == "M" or matrix[row][col] == "C":
        current_deposit = get_deposit(row, col, matrix)
        print(f"{current_deposit} deposit found at ({row}, {col})")
        deposits[current_deposit] += 1

    elif matrix[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        broken = True

success = False
if all(v >= 1 for v in deposits.values()):
    success = True

if success:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
