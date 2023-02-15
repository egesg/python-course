class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()

print(issubclass(A,B)) # Fasle
print(issubclass(B,A)) # True
