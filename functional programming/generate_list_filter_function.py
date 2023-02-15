# Filters do the same, but they take the results and creates a new list with only the true values.

menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffee_starts_with_c(coffee):
    if coffee[0] == "c":
        return coffee

filter_coffee = filter(find_coffee_starts_with_c, menu)
print(filter_coffee)
# <filter object at 0x111a4a020>

for x in filter_coffee:
    print(x)


# cappuccino
# cortado