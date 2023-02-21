from collections import deque

vowels = deque([x for x in input().split(" ")])
consonants = [x for x in input().split(" ")]
current_letters = []
all_flowers = ["rose",
               "tulip",
               "lotus",
               "daffodil",
               ]
found_word = ''
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    current_letters.append(vowel)
    current_letters.append(consonant)
    found = False
    for flower in all_flowers:
        for letter in flower:
            if letter not in current_letters:
                break
        else:
            found = True
            found_word = flower
        if found:
            break
    if found:
        break
if found_word:
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join([x for x in vowels])}")
if consonants:
    print(f"Consonants left: {' '.join([x for x in consonants])}")