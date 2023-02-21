def get_position(player_row, player_col, command):
    if command == "U":
        return player_row - 1, player_col
    if command == "L":
        return player_row, player_col - 1
    if command == "R":
        return player_row, player_col + 1
    if command == "D":
        return player_row + 1, player_col


def is_outside(row, col, rows, cols):
    return row >= rows or col >= cols or row < 0 or col < 0


def get_children(row, col, rows, cols):
    possible_children = [
        [row, col + 1],
        [row, col - 1],
        [row - 1, col],
        [row + 1, col],
    ]
    result = []
    for child_row, child_col in possible_children:
        if not is_outside(child_row, child_col, rows, cols):
            result.append([child_row, child_col])
    return result


rows, cols = [int(x) for x in input().split()]
matrix = []

player_row = 0
player_col = 0
bunnies = set()
for row in range(rows):
    line = list(input())

    for col in range(cols):

        if line[col] == "B":
            bunnies.add(f"{row} {col}")

        elif line[col] == "P":
            player_row = row
            player_col = col

    matrix.append(line)

commands = list(input())
won = False
dead = False

for command in commands:
    next_row, next_col = get_position(player_row, player_col, command)
    matrix[player_row][player_col] = "."

    if is_outside(next_row, next_col, rows, cols):
        won = True

    elif matrix[next_row][next_col] == "B":
        dead = True
        player_row = next_row
        player_col = next_col

    else:
        matrix[next_row][next_col] = "P"
        player_row = next_row
        player_col = next_col

    new_bunnies = set()

    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]
        children = get_children(bunny_row, bunny_col, rows, cols)

        for child_row, child_col in children:
            new_bunnies.add(f"{child_row} {child_col}")
            matrix[child_row][child_col] = "B"

            if child_row == player_row and child_col == player_col:
                dead = True
    bunnies = bunnies.union(new_bunnies)

    if won or dead:
        break

for row in matrix:
    print("".join(row))

if won:
    print(f"won: {player_row} {player_col}")

else:
    print(f"dead: {player_row} {player_col}")
    