player1, player2 = [x for x in input().split(", ")]
rows, cols = 7, 7
matrix = []
throws1 = 0
throws2 = 0
turn = 0
points1 = 501
points2 = 501
for _ in range(rows):
    matrix.append(input().split())


def double_or_triple(total):
    for r in range(rows):
        if matrix[r][col].isdigit():
            total += int(matrix[r][col])
    for c in range(cols):
        if matrix[row][c].isdigit():
            total += int(matrix[row][c])
    return total


def points_deducting(row, col, points):
    total = 0
    if matrix[row][col] == "D":
        total = double_or_triple(total)
        points -= total * 2
    elif matrix[row][col].isdigit():
        points -= int(matrix[row][col])
    elif matrix[row][col] == "T":
        total = double_or_triple(total)
        points -= total * 3
    return points


while True:
    row, col = [int(x) for x in input().strip("(").strip(")").split(", ")]
    turn += 1
    if turn % 2 != 0:
        throws1 += 1
        if row >= rows or col >= cols:
            continue
        if matrix[row][col] == "B":
            print(f"{player1} won the game with {throws1} throws!")
            break
        else:
            points1 = points_deducting(row, col, points1)

        if points1 <= 0:
            print(f"{player1} won the game with {throws1} throws!")
            break
    else:
        throws2 += 1
        if row >= rows or col >= cols:
            continue
        if matrix[row][col] == "B":
            print(f"{player2} won the game with {throws2} throws!")
            break
        else:
            points2 = points_deducting(row, col, points2)

        if points2 <= 0:
            print(f"{player2} won the game with {throws2} throws!")
            break
