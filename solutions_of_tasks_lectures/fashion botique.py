box_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
temporary_value = 0
racks = 1
while box_of_clothes:
    cloth = box_of_clothes.pop()
    if cloth + temporary_value == rack_capacity:
        if box_of_clothes:
            temporary_value = 0
            racks += 1
        else:
            break
    elif cloth + temporary_value > rack_capacity:
        racks += 1
        temporary_value = cloth
    else:
        temporary_value += cloth
print(racks)
