number = int(input())
matrix = []
for _ in range(number):
    line = list(input())
    matrix.append(line)
symbol = input()
found = False
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            found = True
            break
        if found:
            break
if not found:
    print(f"{symbol} does not occur in the matrix")
