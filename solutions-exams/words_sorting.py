def words_sorting(*args):
    words = {}
    for el in args:
        total = 0
        for letter in el:
            total += ord(letter)
        words[el] = total
        total = 0
    sum_values = 0
    for v in words.values():
        sum_values += v
    srt_dict = None
    if sum_values % 2 == 0:
        srt_dict = dict(sorted(words.items(), key=lambda x: x[0]))
    else:
        srt_dict = dict(sorted(words.items(), key=lambda x: -x[1]))
    final_str = ''
    for k, v in srt_dict.items():
        final_str += f"{k} - {v}\n"
    return final_str


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

