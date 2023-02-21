def start_spring(**kwargs):
    spring = {}
    for v, k in kwargs.items():
        if k not in spring.keys():
            spring[k] = []
        spring[k].append(v)
    final_str = ''
    srt_dict = dict(sorted(spring.items(), key=lambda x: (-len(x[1]), x[0])))
    for k, v in srt_dict.items():
        final_str += f"{k}:\n"
        for el in sorted(v):
            final_str += f"-{el}\n"
    return final_str


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


