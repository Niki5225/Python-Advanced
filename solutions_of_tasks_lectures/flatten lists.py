sublists = input().split("|")
result = []
for idx in range(len(sublists) - 1, -1 , -1):
    elements = sublists[idx].strip().split()
    result.extend(elements)
print(" ".join(result))