equation = input()
stack = []
for index in range(len(equation)):
    element = equation[index]
    if element == "(":
        stack.append(index)
    elif element == ")":
        last_opening_parentheses = stack.pop()
        print(equation[last_opening_parentheses:index + 1])