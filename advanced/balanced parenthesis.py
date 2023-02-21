from collections import deque

expression = input()
opening_parentheses = deque([])
dictionary = {"(": ")",
              "[": "]",
              "{": "}"
}
balanced = True
for ch in expression:
    if ch in "([{":
        opening_parentheses.append(ch)
    elif not opening_parentheses:
        balanced = False
    else:
        last_opening_bracket = opening_parentheses.pop()
        if dictionary[last_opening_bracket] != ch:
            balanced = False
    if not balanced:
        break
if not balanced or opening_parentheses:
    print("NO")
else:
    print("YES")
