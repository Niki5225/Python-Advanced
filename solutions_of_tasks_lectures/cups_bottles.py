from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(y) for y in input().split()]
wasted_water = 0
filled_every_cup = False
while True:
    if not bottles:
        break
    current_bottle = bottles.pop()
    current_cup = cups[0]
    status_water = current_cup - current_bottle
    if status_water <= 0:
        cups.popleft()
        wasted_water += abs(status_water)
    else:
        while status_water > 0:
            if not bottles:
                break
            new_bottle = bottles.pop()
            status_water -= new_bottle
            if status_water <= 0:
                wasted_water += abs(status_water)
                cups.popleft()
    if not cups:
        filled_every_cup = True
        break
if filled_every_cup:
    print(f"Bottles: {' '.join([str(bottle) for bottle in bottles])}")
else:
    print(f"Cups: {' '.join([str(cup) for cup in cups])}")
print(f"Wasted litters of water: {wasted_water}")