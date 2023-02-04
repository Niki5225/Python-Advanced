def add_songs(*args):
    songs = {}
    for el in args:
        name, lyrics = el
        if name not in songs.keys():
            songs[name] = []
        songs[name] += lyrics
    result = []
    for k, v in songs.items():
        result.append(f"-{k}")
        result.extend(v)
    return '\n'.join([str(x) for x in result])

print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))

