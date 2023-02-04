from collections import deque

numbers = deque()
expression = input().split()
operations = {"+": lambda a, b: a + b,
              "-": lambda a, b: a - b,
              "*": lambda a, b: a * b,
              "/": lambda a, b: a // b}
for ch in expression:
    if ch in "*+-/":
        while len(numbers) > 1:
            left = numbers.popleft()
            right = numbers.popleft()
            numbers.appendleft(operations[ch](left, right))
    else:
        numbers.append(int(ch))
print(numbers.pop())
