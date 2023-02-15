# Programming Paradigms (style of writing a program)

Programming paradigms are a strategy for 
- reducing code complexity and
- determining the flow of execution

There are several different paradigms:
    - Declarative
    - Procedural
    - Object-Oriented (widely used paradigms. Java, Python, C++, etc.)
    - Function
    - Logic
    - Event-Driven
    - Flow-Driven, etc.


##  Programming Styles of Python (Programming Paradigms)
1. Procedural Programming 
2. Functional Programming -> (Functional-Imperative)
3. Object-Oriented Programming 


Functional vs OOP
design


## Modules
( they can also be executed from within the function )

- scope -> modules create a seperate namespace
- reusability -> better than dublication 
- simplicity -> helps avoid inter-dependency among modules

1. built in modules (math)
2. user defined modules


### namespacing and scoping
1. namespacing
- mapping from names to objects

2. scoping
- textual region of a python program where the namespace is direclty accessible
- determines where your name is visible and directly accessible in your program

dictionary -> key : value (example of mapping names and objects)

there are 4 main types of scopes:
local -> enclosed -> global -> built in 

scope resolution: 
- practice of traying to determine which scope a certain variable belongs 
- it follows LEGB rule 
Local -> inside function 
Enclosed
Global -> outside function
Built in 
nonlocal -> special scope in Python that is used within the nested functions only in the condition that it has been defined earlier in the enclosed functions. 