matrix = []
rows, cols = 6, 6

for row in range(rows):
    matrix.append(input().split())

counter = 0
total_points = 0

while counter < 3:
    command = input().strip(")").strip("(").split(", ")
    row, col = int(command[0]), int(command[1])
    if row >= rows or col >= cols:
        counter += 1
        continue
    if matrix[row][col] == "B":
        for r in range(6):
            if matrix[r][col].isdigit():
                total_points += int(matrix[r][col])
        matrix[row][col] = ""
    counter += 1
if total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
elif total_points < 200:
    print(f"Good job! You scored {total_points} points, and you've won Football.")
elif total_points < 300:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
