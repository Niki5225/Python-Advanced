line = input()
occurrences = {}
for element in line:
    if element not in occurrences.keys():
        occurrences[element] = 0
    occurrences[element] += 1
sorted_dict = sorted(occurrences.items())
for k, v in sorted_dict:
    print(f"{k}: {v} time/s")
