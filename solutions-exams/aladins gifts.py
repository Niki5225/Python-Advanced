from collections import deque


def unmatch(result, material, magic):
    changed_res = None
    if result > 499:
        changed_res = result / 2

    if result < 100:
        if result % 2 == 0:
            changed_res = 2 * material + 3 * magic
        else:
            changed_res = 2 * result
    return changed_res


materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

crafted_items = {"Gemstone": 0,
                 "Porcelain Sculpture": 0,
                 "Gold": 0,
                 "Diamond Jewellery": 0
                 }

while magic_levels and materials:
    material = materials.pop()
    magic = magic_levels.popleft()
    result = material + magic

    if result < 100 or result > 499:
        result = unmatch(result, material, magic)

    if 100 <= result < 200:
        crafted_items["Gemstone"] += 1
    elif 200 <= result < 300:
        crafted_items["Porcelain Sculpture"] += 1
    elif 300 <= result < 400:
        crafted_items["Gold"] += 1
    elif 400 <= result < 500:
        crafted_items["Diamond Jewellery"] += 1

if (crafted_items["Gemstone"] != 0 and crafted_items["Porcelain Sculpture"] != 0) \
        or (crafted_items["Diamond Jewellery"] != 0 and crafted_items["Gold"] != 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

srt_dict = sorted(crafted_items.items(), key=lambda x: x[0])
for k, v in srt_dict:
    if v != 0:
        print(f"{k}: {v}")
