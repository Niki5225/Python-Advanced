def students_credits(*args):
    total_credits = 0
    all_courses = {}
    for el in args:
        current_el = el.split("-")
        course_name, credit, max_test_points, points = current_el
        percentage = int(points) / int(max_test_points)
        received_credit = int(credit) * percentage
        all_courses[course_name] = received_credit
        total_credits += received_credit
    sorted_courses = dict(sorted(all_courses.items(), key=lambda x: x[1], reverse=True))
    if total_credits >= 240:
        print(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        needed_credits = (240 - total_credits)
        print(f"Diyan needs {needed_credits:.1f} credits more for a diploma.")
    return "\n".join([f"{x} - {y:.1f}" for x, y in sorted_courses.items()])

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)



