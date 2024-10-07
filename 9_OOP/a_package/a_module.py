# class Vechicle:
#     '''
#     Create a class called Vechicle
    
#     class attribute:engine_type
    
#     def __init__(self,brand,color)
    
#     def description(self)
#     '''
#     engiene_type='EV'   # class attributes
    
#     def __init__(self,brand,color):       #constructor
#         '''
#         Constructor that takes two arguments(brand ,color)
#         '''
#         self.brand=brand                  #instance attribute
#         self.color=color                  # ""
    
#     def description(self):                  # instance method   
#         '''
#         Instance method for showing engiene_type,brand and color
#         '''
#         print('Engiene Type',self.engiene_type)
#         print('Brand',self.brand)
#         print('Color',self.color)
    

class Laptop:
    Operating_system='Windows'
    
    def __init__(self,brand,Ram):
        self.brand=brand
        self.Ram=Ram
        
    def description(self):
        print('Operating system type',self.Operating_system)
        print('Brand',self.brand)
        print('Ram',self.Ram)
        
l1=Laptop('Acer','4 GB')
l1.description()

l2=Laptop('Dell','16 GB')
l2.description()
