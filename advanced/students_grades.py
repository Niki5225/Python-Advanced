number = int(input())
d = {}
for _ in range(number):
    data = input().split()
    name = data[0]
    grade = float(data[1])
    if name not in d.keys():
        d[name] = []
    d[name].append(grade)
for k, v in d.items():
    total_grade = 0
    for element in v:
        total_grade += element
    average_grade = total_grade / len(v)
    str_grades = []
    for x in v:
        str_grades.append(f"{x:.2f}")
    print(f"{k} -> {' '.join(str_grades)} (avg: {average_grade:.2f})")
