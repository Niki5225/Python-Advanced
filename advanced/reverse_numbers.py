numbers = input().split()
stack = []
for element in numbers.copy():
    stack.append(numbers.pop())
print(*stack)