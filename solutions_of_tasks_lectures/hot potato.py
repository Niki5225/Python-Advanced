from collections import deque

kids = deque()
line = input().split()
for element in line:
    kids.append(element)
toss = int(input())
counter = 1
while len(kids) > 1:
    current_kid = kids.popleft()
    if counter == toss:
        print(f"Removed {current_kid}")
        counter = 1
    else:
        kids.append(current_kid)
        counter += 1
winner = kids[0]
print(f"Last is {winner}")