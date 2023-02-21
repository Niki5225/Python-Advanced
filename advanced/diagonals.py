rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
primary_diagonal = []
secondary_diagonal = []

for row in range(rows):
    primary_diagonal.append(matrix[row][row])
for row in range(rows):
    secondary_diagonal.append(matrix[row][rows - 1 - row])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
