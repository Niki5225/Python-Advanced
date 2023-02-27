from string import punctuation


def get_info(line):
    letters_count = 0
    punctuation_marks = 0
    punct_symbols = set(punctuation)
    for el in line:
        if el.isalpha():
            letters_count += 1
        elif el in punct_symbols:
            punctuation_marks += 1

    return letters_count, punctuation_marks


with open("./text.txt", "r") as file, open("./output.text", "w") as result:
    for idx, line in enumerate(file):
        letters, punc_marks = get_info(line)
        result.write(f"Line {idx + 1}: {line.strip()} ({letters})({punc_marks})\n")
