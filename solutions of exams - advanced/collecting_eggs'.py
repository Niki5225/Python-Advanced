from collections import deque

egg_size = deque([int(x) for x in input().split(", ")])
paper_size = deque([int(x) for x in input().split(", ")])
boxes = 0
box_size = 50

while paper_size and egg_size:
    egg = egg_size.popleft()
    paper = paper_size.pop()
    if egg == 13:
        f_paper = paper_size.popleft()
        paper_size.appendleft(paper)
        paper_size.append(f_paper)
        continue
    if egg <= 0:
        paper_size.append(paper)
        continue
    result = egg + paper
    if result <= box_size:
        boxes += 1
if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if egg_size:
    print(f"Eggs left: {', '.join([str(x) for x in egg_size])}")
if paper_size:
    print(f"Pieces of paper left: {', '.join([str(x) for x in paper_size])}")
