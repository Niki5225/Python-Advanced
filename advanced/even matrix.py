rows = int(input())
even_matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    even_matrix.append(row)
print(even_matrix)
