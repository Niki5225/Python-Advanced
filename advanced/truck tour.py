from collections import deque

petrol_pumps = int(input())
pumps = deque([])
for _ in range(petrol_pumps):
    wpetrol, wkm = [int(a) for a in input().split()]
    pumps.append([wpetrol, wkm])

for attempt in range(petrol_pumps):
    trunk = 0
    failed = False
    for petrol, distance in pumps:
        trunk += petrol - distance
        if trunk < 0:
            failed = True
            break
    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
