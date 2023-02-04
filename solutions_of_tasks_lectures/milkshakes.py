from collections import deque

chocolate = [int(x) for x in input().split(", ")]
milk = deque([int(x) for x in input().split(", ")])

milkshakes_counter = 0

while chocolate and milk and milkshakes_counter < 5:
    the_chocolate = chocolate.pop()
    milk_cup = milk.popleft()
    if the_chocolate <= 0 and milk_cup <= 0:
        continue
    if the_chocolate <= 0:
        milk.appendleft(milk_cup)
        continue
    if milk_cup <= 0:
        chocolate.append(the_chocolate)
        continue
    if the_chocolate == milk_cup:
        milkshakes_counter += 1
    else:
        milk.append(milk_cup)
        chocolate.append(the_chocolate - 5)
if milkshakes_counter == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
else:
    print("Milk: empty")
