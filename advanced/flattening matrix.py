flattened_matrix = []
rows = int(input())
for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    for el in row:
        flattened_matrix.append(el)
print(flattened_matrix)