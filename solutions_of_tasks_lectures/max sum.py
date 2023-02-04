import sys

rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
best_sum = -sys.maxsize
starting_row = 0
starting_col = 0
for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2]\
            + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2]\
            + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if current_sum > best_sum:
            best_sum = current_sum
            starting_row = row
            starting_col = col
print(f"Sum = {best_sum}")
print(matrix[starting_row][starting_col], matrix[starting_row][starting_col + 1], matrix[starting_row][starting_col + 2])
print(matrix[starting_row + 1][starting_col], matrix[starting_row + 1][starting_col + 1], matrix[starting_row + 1][starting_col + 2])
print(matrix[starting_row + 2][starting_col], matrix[starting_row + 2][starting_col + 1], matrix[starting_row + 2][starting_col + 2])