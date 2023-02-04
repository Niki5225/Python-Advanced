from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for _ in orders.copy():
    current_order = orders.popleft()
    if food >= current_order:
        food -= current_order
    else:
        orders.appendleft(current_order)
        break

if not orders:
    print(f"Orders complete")
else:
    print(f"Orders left: {' '.join([str(y) for y in orders])}")