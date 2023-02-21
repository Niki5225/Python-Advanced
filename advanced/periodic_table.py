number = int(input())
unique_elements = set()
for _ in range(number):
    line = input().split()
    for element in line:
        unique_elements.add(element)
x = {print(k) for k in unique_elements}