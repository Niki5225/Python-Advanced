from collections import deque

firework_effect = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

crafted_items = {"Palm Fireworks": 0,
                 "Willow Fireworks": 0,
                 "Crossette Fireworks": 0}

completed = False
while firework_effect and explosive_power:
    effect = firework_effect.popleft()
    explosiveness = explosive_power.pop()

    if effect <= 0 and explosiveness <= 0:
        continue
    if effect <= 0:
        explosive_power.append(explosiveness)
        continue
    if explosiveness <= 0:
        firework_effect.appendleft(effect)
        continue

    result = explosiveness + effect

    if result % 5 == 0 and result % 3 == 0:
        crafted_items["Crossette Fireworks"] += 1
    elif result % 3 == 0:
        crafted_items["Palm Fireworks"] += 1
    elif result % 5 == 0:
        crafted_items["Willow Fireworks"] += 1
    else:
        firework_effect.append(effect - 1)
        explosive_power.append(explosiveness)

    if all(x >= 3 for x in list(crafted_items.values())):
        completed = True
        break
if completed:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effect:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effect])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")
for k, v in crafted_items.items():
    print(f"{k}: {v}")
