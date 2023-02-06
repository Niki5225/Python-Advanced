def shopping_cart(*args):
    meals = {'Soup': [],
             'Pizza': [],
             'Dessert': []}
    for tup in args:
        if 'Stop' in tup:
            break
        name = tup[0]
        product = tup[1]
        if name == 'Soup' and len(meals[name]) == 3:
            continue
        if name == 'Pizza' and len(meals[name]) == 4:
            continue
        if name == 'Dessert' and len(meals[name]) == 2:
            continue

        if product in meals[name]:
            continue
        else:
            meals[name].append(product)
    srt_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))
    final_string = ''
    for v in meals.values():
        if len(v) > 0:
            break
    else:
        return "No products in the cart!"
    for k, v in srt_meals:
        final_string += f"{k}:\n"
        srt_v = sorted(v)
        for el in srt_v:
            final_string += f" - {el}\n"
    return final_string


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

