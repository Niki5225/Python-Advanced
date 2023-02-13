def flights(*args):
    destinations = {}
    idx = 0
    last_destination = None
    for el in args:
        if el == "Finish":
            break
        if idx % 2 == 0:
            if el not in destinations.keys():
                destinations[el] = 0
            last_destination = el
        else:
            destinations[last_destination] += int(el)
        idx += 1
    return destinations


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
