number = int(input())

for x in range(number):
    print(" " * (number - x - 1) + "* " * (x + 1))

for y in range(number - 2, -1, -1):
    print(" " * (number - y - 1) + "* " * (y + 1))