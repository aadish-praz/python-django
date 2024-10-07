# def add(*args):
#     return sum(args)

# a=add(1,2)
# print(a)
# b=add(1,2,3)
# print(b)
# c=add(1,2,3,4)
# print(c)

# def myfunction(*args):
#     # print(args)
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)
# myfunction(3,4,5)

# def myfunction(**kwargs):
#     # print(args)
#     sum=0
#     for value in kwargs.values():
#         sum=sum+value
#     print(sum)

#     # return sum
    
    
# myfunction(a=3,b=4,c=5,d=6)


# class Math:
    

#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
        
#     def calculate_area(self):
#         print('Area of Square is',self.length**2)
#         print('Area of Rectangle is',self.length*self.breadth)
        

# m1=Math(1,1)
# m1.calculate_area(5)
    
class Math:
    
    def area(self,l,b=None):
        if b==None:
            print(l*l)
            
        else:
            print(l*b)
            
m=Math()
m.area(5)
m.area(5,4)


