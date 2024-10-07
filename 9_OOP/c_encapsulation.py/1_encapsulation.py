''' Encapsulation '''

'''
1.Public
2.Private
3.Protected
'''


class vechicle:
    
    def __init__(self,engiene_type,brand,color):
        self.engiene_type=engiene_type        #public   no underscore
        self._brand=brand                    #Protected _
        self.__color=color                   #Private __
        
    def description(self):
        print('Engiene type',self.engiene_type)
        print('Brand',self._brand)
        print('color',self.__color)
        
v1=vechicle('EV','BYD','Silver')
# v1.description()


# Access

# print(v1.engiene_type)
# print(v1._brand)           # can access protected but not recommended
# print(v1.__color)

# modifying

# v1.engiene_type='Hybrid'
# print(v1.engiene_type)

# v1.__c='Black'
# print(v1.__c)
# v1.description()

# print(v1._vechicle__color)      #can access private like this but not recommended