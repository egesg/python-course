# Maps take all objects in a list and applies a function.

menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffee_starts_with_c(coffee):
    if coffee[0] == "c":
        return coffee

map_coffee = map(find_coffee_starts_with_c, menu)
print(map_coffee)
# <map object at 0x110d42020>

for x in map_coffee:
    print(x)


# None
# None
# None
# cappuccino
# cortado
# None