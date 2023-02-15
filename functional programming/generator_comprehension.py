# It is also very similar to lists with the variation of using curved brackets instead of square brackets. 
# They are also more memory efficient as compared to list comprehensions.

data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)

print(gen_obj)
# <generator object <genexpr> at 0x10118b9f0>
print(type(gen_obj))
# <class 'generator'>

for items in gen_obj:
    print(items, end = " ")
# 2 3 5 7 11 13 17 19 23 29 31

# I created a generator object of the class generator instead of a list. 
# The elements in this iterator object cannot be directly accessed and need the help of a for loop and as such.
# I iterate over these elements and print them.