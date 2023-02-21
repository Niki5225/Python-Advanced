line = tuple(map(float, input().split()))
values = {}
for element in line:
    if element not in values:
        values[element] = 0
    values[element] += 1
for k, v in values.items():
    print(f"{k} - {v} times")
