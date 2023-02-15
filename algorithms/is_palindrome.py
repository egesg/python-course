# Algorithm for a Palindrome

str = "racecar"

# check if
# str[0] == str[6]
# str[1] == str[5]
# str[2] == str[4]


def isPalindrome(str):
    start_index = 0
    end_index = len(str) - 1

    for x in str:
        if str[start_index] != str[end_index]:
            return False
    return True


print(isPalindrome('racecar'))
# True
print(isPalindrome('racecars'))
# False