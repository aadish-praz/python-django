''' Class Method '''

class Student:
    college_name='khwopa college of engineering'
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show(self):
        print('Name',self.name)
        print('Age',self.age)
        print('College Name',self.college_name)
        
    @classmethod    
    def change_college(cls,new_college):
        cls.college_name=new_college
    # def change_college(self,new_college):
        # Student.college_name=new_college
        
    
        
        
s1=Student('Ram',24)
s1.show()

Student.change_college('khec')
s3=Student('shyam',21)
s3.show()
        
    


