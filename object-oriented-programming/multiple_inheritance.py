class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()

print(c.a, c.b)
# 1 2