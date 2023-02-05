rows, cols = [int(x) for x in input().split(", ")]

matrix = []

row, col = 0, 0

taken_things = {"Christmas decorations": 0,
                "Gifts": 0,
                "Cookies": 0
                }

for row1 in range(rows):
    line = input().split()
    matrix.append(line)
    for col1 in range(len(line)):
        if matrix[row1][col1] == "Y":
            row = row1
            col = col1


def presents_and_mark_position(matrix, row, col):
    if matrix[row][col] == "D":
        taken_things["Christmas decorations"] += 1
    elif matrix[row][col] == "C":
        taken_things["Cookies"] += 1
    elif matrix[row][col] == "G":
        taken_things["Gifts"] += 1
    matrix[row][col] = "x"


def get_position(matrix, row, col, command, steps):
    if command == "left":
        for step in range(steps):
            if any([x != "." and x != "x" for row in matrix for x in row]):
                if col - 1 < 0:
                    col = cols - 1
                else:
                    col -= 1
            presents_and_mark_position(matrix, row, col)
    if command == "right":
        for step in range(steps):
            if any([x != "." and x != "x" for row in matrix for x in row]):
                if col + 1 > cols - 1:
                    col = 0
                else:
                    col += 1
            presents_and_mark_position(matrix, row, col)
    if command == "down":
        for step in range(steps):
            if any([x != "." and x != "x" for row in matrix for x in row]):
                if row + 1 > rows - 1:
                    row = 0
                else:
                    row += 1
            presents_and_mark_position(matrix, row, col)
    if command == "up":
        for step in range(steps):
            if any([x != "." and x != "x" for row in matrix for x in row]):
                if row - 1 < 0:
                    row = rows - 1
                else:
                    row -= 1
            presents_and_mark_position(matrix, row, col)
    matrix[row][col] = "Y"
    return row, col


collected_all = False
while True:
    not_collected = False
    if collected_all:
        print("Merry Christmas!")
        break
    inpt = input()
    if inpt == "End":
        break
    b = inpt.split("-")
    command = b[0]
    steps = int(b[1])
    matrix[row][col] = "x"
    row, col = get_position(matrix, row, col, command, steps)
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "D" or matrix[r][c] == "C" or matrix[r][c] == "G":
                not_collected = True
                break
        if not_collected:
            break
    if not not_collected:
        collected_all = True
        print("Merry Christmas!")
        break
print("You've collected:")
print(f'- {taken_things["Christmas decorations"]} Christmas decorations')
print(f'- {taken_things["Gifts"]} Gifts')
print(f'- {taken_things["Cookies"]} Cookies')

for row in matrix:
    print(*row, sep=" ")
