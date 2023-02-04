from collections import deque


def read_robots():
    robots = {}
    robots_input = input().split(";")
    for a in robots_input:
        data = a.split("-")
        name = data[0]
        process_time = int(data[1])
        robots[name] = process_time
    return robots


def read_product():
    queue = deque()
    while True:
        product = input()
        if product == "End":
            break
        queue.append(product)
    return queue


def to_seconds(hours, minutes, seconds):
    return hours * 60 * 60 + minutes * 60 + seconds


def time_str(seconds):
    a = seconds // 3600
    b = (seconds % 3600) // 60
    c = (seconds % 3600) % 60
    return f"{a:02d}:{b:02d}:{c:02d}"


robots_data = read_robots()
available_robots = [k for k in robots_data.keys()]
processing_robots = {}
time = [int(x) for x in input().split(":")]
time_seconds = to_seconds(time[0], time[1], time[2])
products = read_product()

while products:
    time_seconds = (time_seconds + 1) % (24 * 60 * 60)
    for robot in [k for k in processing_robots.keys()]:
        processing_robots[robot] -= 1
        if processing_robots[robot] <= 0:
            processing_robots.pop(robot)

    current_product = products.popleft()

    for robot in available_robots:
        if robot not in processing_robots.keys():
            print(f"{robot} - {current_product} [{time_str(time_seconds)}]")
            processing_robots[robot] = robots_data[robot]
            break
    else:
        products.append(current_product)
