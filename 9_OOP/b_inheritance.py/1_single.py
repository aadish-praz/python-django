# Single Inheritance

class A:
    def show(self):
        print('base class A')
class B(A):
    pass

b=B()
b.show()