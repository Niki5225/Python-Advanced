text = input()
stack = []
for element in text[::-1]:
    stack.append(element)
print("".join(stack))