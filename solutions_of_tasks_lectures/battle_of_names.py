number = int(input())
even = set()
odd = set()

for row in range(1, number + 1):
    name = input()
    total = 0
    for el in name:
        total += ord(el)
    total = total // row
    if total % 2 == 0:
        even.add(total)
    else:
        odd.add(total)
sum_even = sum(even)
sum_odd = sum(odd)

if sum_even == sum_odd:
    print(', '.join([str(x) for x in even.union(odd)]))
elif sum_odd > sum_even:
    print(', '.join([str(x) for x in odd.difference(even)]))
elif sum_even > sum_odd:
    print(', '.join([str(x) for x in odd.symmetric_difference(even)]))
