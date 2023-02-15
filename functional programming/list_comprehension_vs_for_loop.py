data = [2,3,5,7,11,13,17,19,23,29,31]

# List comprehension:
data = [x+3 for x in data]
print("Updating the list: ", data)
# Updating the list:  [5, 6, 8, 10, 14, 16, 20, 22, 26, 32, 34]


# Regular for loop:
for x in range(len(data)):
    data[x] = data[x] + 3
print(data)
# [5, 6, 8, 10, 14, 16, 20, 22, 26, 32, 34]