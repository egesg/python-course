'''
class Recipe():
    def __new__(cls: type[Self]) -> Self:
        pass

    def __init__(self) -> None:
        pass
'''

class Recipe():
    def __init__(self,dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        return (f'The {self.dish} has {str(self.items)} and takes {str(self.time)} min to prepare.')

pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

print(pizza.items)
# ['cheese', 'bread', 'tomato']
print(pasta.items)
# ['penne', 'sauce']
print(pizza.contents())
# The Pizza has ['cheese', 'bread', 'tomato'] and takes 45 min to prepare.
print(pasta.contents())
# The Pasta has ['penne', 'sauce'] and takes 55 min to prepare.