class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_of_rooms = 5
    bathrooms = 2
    
house = House()
print(house)
# <__main__.House object at 0x1108c1350>
print(house.num_of_rooms)
# 5
print(House.num_of_rooms)
# 5

house.num_of_rooms = 7
print(house.num_of_rooms)
# 7
print(House.num_of_rooms)
# 5

House.num_of_rooms = 7
print(house.num_of_rooms)
# 7
print(House.num_of_rooms)
# 7