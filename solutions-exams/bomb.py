from collections import deque

bomb_effects = deque([int(x) for x in input().split(",")])
bomb_casings = deque([int(x) for x in input().split(",")])

all_bombs_crafted = {"Datura Bombs": 0,
                     "Cherry Bombs": 0,
                     "Smoke Decoy Bombs": 0
                     }
completed = False
while bomb_effects and bomb_casings:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()
    result = effect + casing
    if result == 40:
        all_bombs_crafted["Datura Bombs"] += 1
    elif result == 60:
        all_bombs_crafted["Cherry Bombs"] += 1
    elif result == 120:
        all_bombs_crafted["Smoke Decoy Bombs"] += 1
    else:
        bomb_effects.appendleft(effect)
        bomb_casings.append(casing - 5)
    if all(x >= 3 for x in list(all_bombs_crafted.values())):
        completed = True
        break
if completed:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")
for k, v in sorted(all_bombs_crafted.items()):
    print(f"{k}: {v}")