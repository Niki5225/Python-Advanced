from collections import deque

quantity_water_liters = int(input())
people = deque()
while True:
    line = input()
    if line == "Start":
        break
    people.append(line)
while True:
    line = input()
    if line == "End":
        break
    current_line = line.split()
    if len(current_line) == 2:
        liters = int(current_line[1])
        quantity_water_liters += liters
    else:
        liters = int(current_line[0])
        person_name = people.popleft()
        if liters <= quantity_water_liters:
            quantity_water_liters -= liters
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
print(f"{quantity_water_liters} liters left")
