from collections import deque

miligrams_caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])
caffeine_for_the_day = 0

while miligrams_caffeine and energy_drinks:
    current_drink = energy_drinks.popleft()
    current_caffeine = miligrams_caffeine.pop()
    result = current_caffeine * current_drink

    if caffeine_for_the_day + result <= 300:
        caffeine_for_the_day += result
    else:
        energy_drinks.append(current_drink)
        if caffeine_for_the_day - 30 >= 0:
            caffeine_for_the_day -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {caffeine_for_the_day} mg caffeine.")
