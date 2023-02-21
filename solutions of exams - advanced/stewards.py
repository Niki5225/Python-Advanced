from collections import deque

seats = input().split(", ")
first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])
rotations = 0
matches = []

while rotations < 10 and len(matches) < 3:
    first_num = first_sequence.popleft()
    second_num = second_sequence.pop()
    rotations += 1
    asci_char = chr(first_num + second_num)
    possible_matches = [f"{first_num}{asci_char}", f"{second_num}{asci_char}"]
    for el in possible_matches:
        if el in seats:
            matches.append(el)
            seats.remove(el)
            continue
        first_sequence.append(first_num)
        second_sequence.appendleft(second_num)
print(f"Seat matches: {', '.join([str(x) for x in matches])}")
print(f"Rotations count: {rotations}")