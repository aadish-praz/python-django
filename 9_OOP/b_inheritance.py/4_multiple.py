# # Multiple

class B():
    def show(self):
        print('base class B')

class C():
    pass

class D(B,C):
    pass

d=D()
d.show()