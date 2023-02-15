# It is trying to locate an item from the list that does not exist. 
# Running the code will throw the IndexError. 
# Add exception handling to stop the error from being thrown and return a more user-friendly message such as "Item does not exist in the list".

items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except:
    print("Item does not exist in the list")


# Item does not exist in the list