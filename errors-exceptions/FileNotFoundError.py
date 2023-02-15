# It is looking for a file that does not exist. 
# Add exception handling to catch this error and return the following "The file could not be found".

try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())

except FileNotFoundError:
    print("Unable to locate file")


# Unable to locate file