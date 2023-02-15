# help function

class A:
    num = 5

class B(A):
    num = 9

class C(B):
    pass

print(help(C))

'''
Help on class C in module __main__:

class C(B)
 |  Method resolution order:
 |      C
 |      B
 |      A
 |      builtins.object
 |  
 |  Data and other attributes inherited from B:
 |  
 |  num = 9
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from A:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
'''
