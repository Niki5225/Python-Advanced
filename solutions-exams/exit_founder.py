player1, player2 = input().split(", ")
matrix = []
for row in range(6):
    matrix.append(input().split())
rotations = 0
even_rotations = False
player1_next_move_ignored = False
player2_next_move_ignored = False
while True:
    row, col = [int(x) for x in input().strip("(").strip(")").split(", ")]
    rotations += 1
    if rotations % 2 == 0:
        even_rotations = True
    else:
        even_rotations = False

    if even_rotations:
        if player2_next_move_ignored:
            player2_next_move_ignored = False
            continue
    else:
        if player1_next_move_ignored:
            player1_next_move_ignored = False
            continue

    if matrix[row][col] == "E":
        if even_rotations:
            print(f"{player2} found the Exit and wins the game!")
            break
        else:
            print(f"{player1} found the Exit and wins the game!")
            break
    elif matrix[row][col] == "T":
        if even_rotations:
            print(f"{player2} is out of the game! The winner is {player1}.")
            break
        else:
            print(f"{player1} is out of the game! The winner is {player2}.")
            break
    elif matrix[row][col] == "W":
        if even_rotations:
            print(f"{player2} hits a wall and needs to rest.")
            player2_next_move_ignored = True
        else:
            print(f"{player1} hits a wall and needs to rest.")
            player1_next_move_ignored = True
