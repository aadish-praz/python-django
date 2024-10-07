''' Method Overiding '''

class People:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def description(self):
        print('Name',self.name)
        print('Age',self.age)
        

class Employee(People):
    
    def __init__(self,name,age,salary,address):
        super().__init__(name,age)
        self.salary=salary
        self.address=address
        
    def description(self):
        super().description()
        print('Salary',self.salary)
        print('Address',self.address)
        
e=Employee('Ram',20,20000,'bhaktapur')
e.description()
        