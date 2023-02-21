rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

primary_diagonal_sum = 0
for idx in range(rows):
    primary_diagonal_sum += matrix[idx][idx]
print(primary_diagonal_sum)