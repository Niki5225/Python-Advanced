black_row = 0
black_col = 0
white_row = 0
white_col = 0
matrix = []

for row in range(8):
    matrix.append(input().split())

coordinates_b = False
coordinates_w = False

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 'w':
            white_row = row
            white_col = col
            coordinates_w = True
        elif matrix[row][col] == 'b':
            black_col = col
            black_row = row
            coordinates_b = True
    if coordinates_w and coordinates_b:
        break

rotations = 0
white_move = False


def get_position(row):
    if white_move:
        return row - 1
    else:
        return row + 1


while True:
    rotations += 1
    if rotations % 2 != 0:
        white_move = True
    else:
        white_move = False

    if white_move:
        if (white_row - 1, white_col - 1) == (black_row, black_col) \
                or (white_row - 1, white_col + 1) == (black_row, black_col):
            print(f"Game over! White win, capture on {chr(97 + black_col)}{abs(black_row - 8)}.")
            break
        matrix[white_row][white_col] = "-"
        white_row = get_position(white_row)
        matrix[white_row][white_col] = "w"
        if white_row == 0:
            print(f"Game over! White pawn is promoted to a queen at {chr(97 + white_col)}8.")
            break
    else:
        if (black_row + 1, black_col + 1) == (white_row, white_col) \
                or (black_row + 1, black_col - 1) == (white_row, white_col):
            print(f"Game over! Black win, capture on {chr(97 + white_col)}{abs(white_row - 8)}.")
            break
        matrix[black_row][black_col] = "-"
        black_row = get_position(black_row)
        matrix[black_row][black_col] = "b"
        if black_row == len(matrix) - 1:
            print(f"Game over! Black pawn is promoted to a queen at {chr(97 + black_col)}1.")
            break