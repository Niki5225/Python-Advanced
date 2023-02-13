def shopping_list(*args, **kwargs):
    budget = None
    basket = 0
    bought_product_str = ''
    for el in args:
        budget = el
    if budget < 100:
        return "You do not have enough budget."

    for k, v in kwargs.items():
        if basket == 5:
            break
        price, quantity = v[0], v[1]
        if price * quantity <= budget:
            budget -= price * quantity
            bought_product_str += f"You bought {k} for {price * quantity:.2f} leva.\n"
            basket += 1
    return bought_product_str


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

