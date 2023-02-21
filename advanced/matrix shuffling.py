rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    line = input()
    if line == "END":
        break
    commands = line.split()
    if commands[0] != "swap" or len(commands) > 5:
        print("Invalid input!")
        continue
    rows1, cols1, rows2, cols2 = [int(x) for x in commands[1:]]
    if rows1 >= rows or rows2 >= rows or cols1 >= cols or cols2 >= cols or rows1 < 0 or rows2 < 0 or cols1 < 0 or cols2 < 0:
        print("Invalid input!")
        continue
    matrix[rows1][cols1], matrix[rows2][cols2] = matrix[rows2][cols2], matrix[rows1][cols1]
    for row in matrix:
        print(*row, sep=" ")