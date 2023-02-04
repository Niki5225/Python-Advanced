from collections import deque

bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
operators = deque([x for x in input().split()])

operations = {"+": lambda a, b: a + b,
              "-": lambda a, b: a - b,
              "*": lambda a, b: a * b,
              "/": lambda a, b: a / b}
honey = 0
while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()
    if nectar < bee:
        bees.appendleft(bee)
        continue
    if nectar == 0:
        continue
    operator = operators.popleft()
    honey += abs(operations[operator](bee, nectar))

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")