matrix = []
for row in range(6):
    line = input().split()
    matrix.append(line)

location = input().strip("(").strip(")").split(", ")
row = int(location[0])
col = int(location[1])


def get_position(direction, row, col):
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1


while True:
    line = input()
    if line == "Stop":
        break
    cur_line = line.split(", ")
    command = cur_line[0]
    direction = cur_line[1]
    if command == "Create":
        value = cur_line[2]
        row, col = get_position(direction, row, col)
        if matrix[row][col] == ".":
            matrix[row][col] = value

    elif command == "Update":
        value = cur_line[2]
        row, col = get_position(direction, row, col)
        if matrix[row][col].isdigit() or matrix[row][col].isalpha():
            matrix[row][col] = value
    elif command == "Delete":
        row, col = get_position(direction, row, col)
        if matrix[row][col].isdigit() or matrix[row][col].isalpha():
            matrix[row][col] = "."
    elif command == "Read":
        row, col = get_position(direction, row, col)
        if matrix[row][col].isdigit() or matrix[row][col].isalpha():
            print(matrix[row][col])
for row in matrix:
    print(' '.join([str(x) for x in row]))
