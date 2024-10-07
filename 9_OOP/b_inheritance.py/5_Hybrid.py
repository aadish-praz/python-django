# Hybrid

class A():
    def show(self):
        print('base class A')

class B(A):
    pass
    

class C(A):
    pass

class D(B,C):
    pass

class E(D):
    pass

e=E()
e.show()

print(E.mro())