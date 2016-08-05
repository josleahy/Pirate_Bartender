import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def find_pref():
    preferences = {}
    for key, value in questions.items():
        user_input = input(value + '')
        preferences[key] = (user_input.lower() == "y" or user_input.lower() == "yes")
    return preferences

def mix_drink(value):
    my_drink = []
    for key, value in value.items():
        if value == True:
            my_drink.append(random.choice(ingredients[key]))
    return my_drink

def main():
    results = find_pref()
    print("\nGreat, I reccomend a: ")
    for drink in mix_drink(results):
        print(drink)
main()

