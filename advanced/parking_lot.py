parking_lot = set()
number = int(input())
for _ in range(number):
    command, plate = input().split(", ")
    if command == "IN":
        parking_lot.add(plate)
    else:
        if plate in parking_lot:
            parking_lot.remove(plate)
if parking_lot:
    a = {print(x) for x in parking_lot}
else:
    print("Parking Lot is Empty")
