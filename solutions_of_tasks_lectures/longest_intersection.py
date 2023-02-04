number = int(input())
largest_set = set()
for _ in range(number):
    first, second = input().split("-")

    first_start, first_end = [int(x) for x in first.split(",")]
    second_start, second_end = [int(x) for x in second.split(",")]

    first_set = {int(y) for y in range(first_start, first_end + 1)}
    second_set = {int(y) for y in range(second_start, second_end + 1)}
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(largest_set):
        largest_set = intersection
print(f"Longest intersection is [{', '.join([str(x) for x in largest_set])}] "
      f"with length {len(largest_set)}")
