number = int(input())
invited = {input() for _ in range(number)}
came = set()
while True:
    line = input()
    if line == "END":
        break
    came.add(line)
did_not_come = invited.difference(came)
print(len(did_not_come))
a = {print(x) for x in sorted(did_not_come)}