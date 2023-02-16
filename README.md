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


## Packages - Libraries - Frameworks

- popular packages: json, numpy, pandas, NLTK (Natural Language Processing)

- data analysis packages: 
numpy, 
scipy, 
matplotlib: visualization -> ggplot, seaborn
scikit-learn: predictive learning, supervised and unsupervised ML algorithms classification, regression, SVM's
pandas: series (single dimentional) and dataframes (multi dimentional)
plotly

- machine learning is subsection of AI:
natural language processing
deep learning
sentiment analysis
recommender engines
computer vision
speech recognition

- web frameworks
fullstack: django, web2py, pyramid
migroframeworks: flask, bottle, dash, cherrypy
asysnchronous: growler, AIOHTTP, sanic

## Testing
types of testing
- unit
- integration
- system
- acceptance testing

ways to categorize different test types
1. 
- white box -> knowledge of the code design and functionalities
- black box

2.
- functional tests -> they determine if the features and functionalities are in line with the expectations
- non-functional tests -> more complex to define and involves metricts suchs as overall performance and quality
- maintenance tests -> when the system and its operational environment is corrected, changed, or extended


### test automation packages
some important python testing frameworks
- unittest -> built in testing package
- pytest -> native python library
- robot -> keyword-driven developmeent capabilities
- selenium -> web applications

### Test-driven development (TDD)
write the test first, and the the code, so that the tests will pass
- pytest -> only requires writing functions
- unittest -> requires classses, it has useful libraries such as unittest.mock that can mock large functions, removing the time and memory overhead.

2. TDD vs conventional testing
- TDD -> requirements and standards are highligheted from the beginning
behavior-driven
acceptance driven
scaling
developer test driven
- conventional testing ->

3. Applying TDD
