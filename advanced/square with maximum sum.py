import sys

rows, cols = [int(x) for x in input().split(", ")]
matrix = []
starting_row = 0
starting_col = 0
best_sum = -sys.maxsize
submatrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for row in range(rows - 1):
    for col in range(cols - 1):
        the_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if the_sum > best_sum:
            starting_row = row
            starting_col = col
            best_sum = the_sum
print(matrix[starting_row][starting_col], matrix[starting_row][starting_col + 1])
print(matrix[starting_row + 1][starting_col], matrix[starting_row + 1][starting_col + 1])
print(best_sum)