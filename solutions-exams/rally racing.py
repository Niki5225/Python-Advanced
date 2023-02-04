def get_position(row, col, line):
    if line == "up":
        return row - 1, col
    if line == "left":
        return row, col - 1
    if line == "right":
        return row, col + 1
    if line == "down":
        return row + 1, col


size = int(input())
racing_number = input()
car_row = 0
car_col = 0
matrix = []

for _ in range(size):
    matrix.append(input().split())

kilometers_passed = 0
found_tunnel = False

while True:
    line = input()
    if line == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    next_row, next_col = get_position(car_row, car_col, line)

    if matrix[next_row][next_col] == ".":
        kilometers_passed += 10
        matrix[car_row][car_col] = "."
        car_row, car_col = next_row, next_col

    elif matrix[next_row][next_col] == "T":
        matrix[next_row][next_col] = "."

        for row in range(size):
            for col in range(size):

                if matrix[row][col] == "T":
                    matrix[row][col] = "."
                    car_row, car_col = row, col
                    found_tunnel = True

            if found_tunnel:
                break
        kilometers_passed += 30

    elif matrix[next_row][next_col] == "F":
        kilometers_passed += 10
        car_row, car_col = next_row, next_col
        print(f"Racing car {racing_number} finished the stage!")
        break

print(f"Distance covered {kilometers_passed} km.")
matrix[car_row][car_col] = "C"

for row in matrix:
    print(''.join(row))
