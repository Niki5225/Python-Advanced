from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

crafting_table = {150: "Doll",
                  250: "Wooden train",
                  300: "Teddy bear",
                  400: "Bicycle"}
toys = {}

while magic and materials:
    material = materials.pop()
    value = magic.popleft()
    result = material * value
    if value == 0 and material == 0:
        continue
    if value == 0:
        materials.append(material)
        continue
    if material == 0:
        magic.appendleft(value)
        continue
    if result in crafting_table.keys():
        toy_name = crafting_table[result]
        if toy_name in toys:
            toys[toy_name] += 1
            continue
        else:
            toys[toy_name] = 1
            continue
    if result < 0:
        materials.append(material + value)
    else:
        materials.append(material + 15)
if ("Doll" in toys and "Wooden train" in toys) or ("Teddy bear" in toys and "Bicycle" in toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")
for toy, count in sorted(toys.items()):
    print(f"{toy}: {count}")
