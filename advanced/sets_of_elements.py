n, m = [int(x) for x in input().split()]
first_set = {int(input()) for y in range(n)}
second_set = {int(input()) for z in range(m)}
intersection = first_set.intersection(second_set)
for element in intersection:
    print(element)