from collections import deque

green_light_duration = int(input())
free_window = int(input())
cars = deque()
cars_counter = 0
crashed = False
while True:
    line = input()
    if line == "END":
        break
    if line == "green":
        if cars:
            current_car = cars.popleft()
            last_seconds = green_light_duration - len(current_car)
            while last_seconds > 0:
                if not cars:
                    break
                current_car = cars.popleft()
                cars_counter += 1
                last_seconds -= len(current_car)
            if last_seconds == 0:
                cars_counter += 1
            elif free_window >= abs(last_seconds):
                cars_counter += 1
            else:
                crashed = True
                crash = free_window - abs(last_seconds)
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[crash]}.")
                break
    else:
        cars.append(line)
if not crashed:
    print(f"Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")
