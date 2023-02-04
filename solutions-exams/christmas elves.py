from collections import deque

elf_energy = deque([int(x) for x in input().split()])
materials_in_box = [int(x) for x in input().split()]
turn = 0
total_energy = 0
toys = 0

while elf_energy and materials_in_box:
    energy = elf_energy.popleft()

    if energy < 5:
        continue

    materials = materials_in_box.pop()
    turn += 1

    if turn % 3 == 0 and turn % 5 == 0:
        if energy >= materials * 2:
            total_energy += materials * 2
            elf_energy.append(energy - materials * 2)
        else:
            elf_energy.append(energy * 2)
            materials_in_box.append(materials)

    elif turn % 3 == 0:
        if energy >= materials * 2:
            total_energy += materials * 2
            elf_energy.append(energy - ((materials * 2) - 1))
            toys += 2
        else:
            elf_energy.append(energy * 2)
            materials_in_box.append(materials)

    elif turn % 5 == 0:
        if energy >= materials:
            total_energy += materials
            elf_energy.append(energy - materials)
        else:
            elf_energy.append(energy * 2)
            materials_in_box.append(materials)
    else:
        if energy >= materials:
            total_energy += materials
            elf_energy.append(energy - (materials - 1))
            toys += 1
        else:
            elf_energy.append(energy * 2)
            materials_in_box.append(materials)
print(f"Toys: {toys}")
print(f"Energy: {total_energy}")
if elf_energy:
    print(f"Elves left: {', '.join(str(x) for x in elf_energy)}")
if materials_in_box:
    print(f"Boxes left: {', '.join(str(x) for x in materials_in_box)}")
