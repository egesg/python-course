# mro function

class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.mro())

# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

