from collections import deque
text = deque(input().split())
main_colours = ["red", "blue", "yellow"]
secondary_colours = ["orange", "purple", "green"]
found_colours = []
while text:
    final_part = ''
    if len(text) > 1:
        final_part = text.pop()
    first_part = text.popleft()
    for colour in (first_part + final_part, final_part + first_part):
        if colour in main_colours or colour in secondary_colours:
            found_colours.append(colour)
            break
    else:
        for item in (final_part[:-1], first_part[:-1]):
            if item:
                text.insert(len(text) // 2, item)
                text.insert(len(text) // 2, item)
for element in found_colours:
    if element == "orange":
        if "red" not in found_colours or "yellow" not in found_colours:
            found_colours.remove(element)
    elif element == "purple":
        if "red" not in found_colours or "blue" not in found_colours:
            found_colours.remove(element)
    elif element == "green":
        if "blue" not in found_colours or "yellow" not in found_colours:
            found_colours.remove(element)
print(found_colours)
