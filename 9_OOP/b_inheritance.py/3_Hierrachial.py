# # Hierarchical

class A:
    def show(self):
        print('base class A')
        
class B(A):
    pass

class C(A):
    pass

b=B()
b.show()

c=C()
c.show()
