from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]
pizzas_made = 0

while pizza_orders and employees:
    order = pizza_orders.popleft()
    if order <= 0 or order > 10:
        continue

    employee = employees.pop()

    if employee >= order:
        pizzas_made += order
        continue
    else:
        order -= employee
        pizzas_made += employee
        pizza_orders.appendleft(order)
if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    if employees:
        print(f"Employees: {', '.join([str(x) for x in employees])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")