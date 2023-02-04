def get_position(row, col, command):
    if command == "up":
        return row - 1, col
    if command == "left":
        return row, col - 1
    if command == "right":
        return row, col + 1
    if command == "down":
        return row + 1, col


size = int(input())

matrix = []
mines = set()
cruisers = []
hits = 0
failed = False
success = False
submarine_row = 0
submarine_col = 0
for row in range(size):
    line = list(input())
    for col in range(size):
        if line[col] == "C":
            cruisers.append(f"{row} {col}")
        elif line[col] == "*":
            mines.add(f"{row} {col}")
        elif line[col] == "S":
            submarine_row, submarine_col = row, col
    matrix.append(line)

while True:
    command = input()
    next_row, next_col = get_position(submarine_row, submarine_col, command)
    matrix[submarine_row][submarine_col] = "-"
    if matrix[next_row][next_col] == "-":
        submarine_row, submarine_col = next_row, next_col
        matrix[submarine_row][submarine_col] = "S"

    elif matrix[next_row][next_col] == "*":
        matrix[next_row][next_col] = "S"
        submarine_row, submarine_col = next_row, next_col
        hits += 1
        if hits == 3:
            failed = True
    elif matrix[next_row][next_col] == "C":

        for cruiser in cruisers:
            cruiser_row, cruiser_col = [int(x) for x in cruiser.split()]
            if cruiser_row == next_row and cruiser_col == next_col:
                cruisers.remove(cruiser)
                matrix[cruiser_row][cruiser_col] = "S"
                submarine_row, submarine_col = cruiser_row, cruiser_col
                break
                
        if not cruisers:
            success = True

    if failed or success:
        break

if success:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
else:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_row}, {submarine_col}]!")
for row in matrix:
    print(''.join(row))
