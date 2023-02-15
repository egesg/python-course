# Functional Programming

## Functions (Standalone / independent)

1. Pure Functions

does not change or have any effect on a variable, data, list, or sets beyond its own scope

Benefits of pure functions:
- known outcome
- consistent and reliable
- cache
- multi-threaded programs


2. Traditional Functions


Traditional         vs          Pure
Access global state             x
Modify global variables         x
Accesss local state             Accesss local state
Change args                     x
x                               Output depends on input


## Comprehensions
a way to create a new sequence from an already existing sequence

There are four main types of comprehensions in Python:
1. List Comprehension
2. Dictionary Comprehension
3. Set Comprehension
4. Generator Comprehension


### map() function vs list comprehensions

1. newdata = map(square, data)
2. newdata = [x + 3 for x in data]

- Both map() functions and list comprehension effectively do the same job of modifying iterator sequences.
- Comprehensions have gained popularity primarily for providing cleaner code readability and ease of use. 
- They also provide some added advantages such as providing filtering using if else conditions.
- List comprehensions also provide direct return of a list as compared to map() function that returns a map object. 
- It is mainly the clarity that has made list comprehensions popular, but map() functions are still arguably a better choice when it comes to the use of larger sequences.