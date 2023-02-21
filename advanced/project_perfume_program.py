brand = input("Hey there! For what brand are you searching for?")

all_perfumes_in_the_perfumery = {"Yves Saint Laurent": {"La Nuit de l'homme": 3,
                                                        "Le perfum": 3,
                                                        "Mon Paris": 17},
                                 "Dolce and Gabanna": {"The One": 7,
                                                       "Light Blue": 4}}
all_perfumes_in_all_shops = {"Yves Saint Laurent": {"La Nuit de l'homme": 3,
                                                    "Le perfum": 3,
                                                    "Mon Paris": 17},
                             "Dolce and Gabanna": {"The One": 7,
                                                   "Light Blue": 4},
                             "Giorgio Armani": {"Code": 8}}
finished = False
while True:
    if brand not in all_perfumes_in_the_perfumery.keys():
        print(f"The brand you searched for is not available in your perfumery.Should I check for it in the others?")
        decision = input()
        if decision == "yes":
            if brand in all_perfumes_in_all_shops.keys():
                print("They have that brand. What is the searched model? ")
                model = input()
                if model in all_perfumes_in_all_shops[brand]:
                    print(f"The perfume of {brand} {model} has {all_perfumes_in_all_shops[brand][model]} in stock."
                          f"You can call them to deliver it. Have a nice day!")
                    finished = True
                    break
        elif decision == "no":
            print("Do you want to search for something else?")
            second_decision = input()
            if "no" == second_decision.lower():
                print("Ok.See you soon!")
                finished = True
                break
            elif "yes" == second_decision:
                perfume = input("Ok, what it will be? ")
                if perfume in all_perfumes_in_all_shops.keys():
                    print(f"The perfume of {brand} {perfume} has {all_perfumes_in_all_shops[brand][perfume]} in stock."
                          f"You can call them to deliver it. Have a nice day!")
                else:
                    print("Sorry,it's not here! Have a nice day!")
                    finished = True
                    break
    else:
        print("You have that brand available. For what model you will search?")
        model = input()
        if model in all_perfumes_in_the_perfumery[brand]:
            print(f"You have it.Left {all_perfumes_in_the_perfumery[brand][model]}")
            break
        else:
            print(f"You don't have it.")
            finished = True
            break
    if finished:
        break