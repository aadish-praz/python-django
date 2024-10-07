

# mylist=[1,2,'john',2.3,[1,2,3],(3,5,'ram')]
# print(mylist)

# mytuple=(1,2,2.3,'john',[1,2,3],(3,2))

# myset={1,3.4,5,'jimmy',(1,2,4)}

# mydict={'a':'john','b':5,'c':2.3}


# mylist=[1,2,1,2,'john',2.3,[1,2,3],(3,5,'ram')]

# mytuple=(1,1,2,32,2.3,'john',[1,2,3],(3,2))

# myset={1,1,1,3.4,5,'jimmy',(1,2,4)} # only immutable and noduplicates

#myset={'apple','banana','cherry','orange'}

#  # variable a will be replace by jim (keys must be unique)

# mylist = list()
# mytuple = tuple()  #casting or constructor
# myset = set()
# mydict = dict()

# print(type(mylist))
# print(type(mytuple))
# print(type(myset))        #can't give indexing as value changes regulary
# print(type(mydict))       #Indexing is done accoring to the key value


''' LIST PRACTICE'''

''' using list comprehesion '''
# import time
# start=time.time()
# mylist=[i for i in range(1,100000000)]
# end=time.time()
# print(f'time taken{end-start}')
#print(mylist)

# mylist=[1,2,3,'john','True','False']


''' Using loop for Dynamically using list'''
# start=time.time()
# mylist=[]
# for i in range (1,100000000):
#     mylist.append(i)
# end=time.time()
# print(f'time taken {end-start}')
#print(mylist)

''' Heterogenous list '''
# mylist=[1,2,4,[3,4,5,6],'john','wick']
# print(mylist)

# list3 = ['a','b','c','d','e','f','g','h','i','j']
#list3= ['0','1','2','3','4','5','6','7','8','9']

# indexing
# print(list3[1])    #b    values
# print(list3[8])    #i values

# print(list3[1:7])   #'b','c','d','e','f','g'               list
# print(list3[3:9])   #'d','e','f','g','h','i'                list
# print(list3[7:2])   #empty list                            list
# print(list3[:9])    #'a','b','c','d','e','f','g','h','i'
# print(list3[4:])    #'e','f','g','h','i','j'
# print(list3[0::2])  #a,c,e,g,i

# print(list3[-3])      # h                               values
# print(list3[-1:-8])   #empty list
# print(list3[-6:-1])   #'e','f','g','h','i'
# print(list3[::-1])    # j,i,h,g,f,e,d,c,b,a
# print(list3[-1:-8:-1]) # j.....d


''' index,count,append,insert,extend'''
# list0=['a','b','c','d','d']
# list1=['d','e','f','g']

# print(list0.index('a'))
# print(list0.count('d'))

# list0.append('e')
# print(list0)

# list0.insert(1,['x','y'])
# print(list0)

# list0.extend(list1)
# print(list0)

 
'''pop remove clear'''
 
# list0=['a','b','c','d','e']

# result=list0.pop(1)
# print(list0)
# print(result)

# list0.remove('a')
# print(list0)

# list0.clear()
# print(list0)

''' reverse ,sort'''

# list0=['a','b','e','f','e']

# list0.reverse()
# print(list0)

# list0.sort()
# print(list0)

''' copy {Assignment copy, shallow copy, Deep copy}'''


# from copy import deepcopy

# list=['a','b','e','f','e',[1,2,3]]

# assign_copy=list
# shallow_copy=list.copy()
# deep_copy=deepcopy(list)



# list[1]='c'
# list[5][1]=11


# print(assign_copy)
# print(shallow_copy)
# print(deep_copy)

# print(id(list))
# print(id(assign_copy))
# print(id(shallow_copy))
# print(id(deep_copy))
# thisdict = { "brand": "Ford", 
# "model": "Mustang", 
# "year": 1964, 
# "year": 2020 } 
# print(len(thisdict))



# x= lambda a:a+10
# print(x(10))

# multiply=lambda x,y:x*y
# print(multiply(5,6))

# numbers=[1,2,3,4]
# square=map(lambda x:x**2,numbers)
# print(list(square))

# numbers=[1,2,3,4]
# even=filter(lambda x:x%2==0,numbers)
# print(list(even))

# def make_adder(n):
#     return lambda x:x+n
# add=make_adder(5)
# print(add(5))


# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# def fibonacci(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
    
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
    
# print(fibonacci(6))

# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
    
# n=0

# while fibonacci(n)<1000:
#     print(fibonacci(n),end=' ')
#     n+=1
    




'''
Task 1
Create a decorator authorized that checks if a user is authorized before allowing a function to execute.


'''


# def authorized(fx1):
#     def inner_function(*args,**kwargs):
#         # print(args)
#         if args[0]=='admin':
#             fx1(*args,**kwargs)
#         else:
#             print('unauthorized access')
                    
#     return inner_function
                
                  
# @authorized
# def delete_user_data(user):
#     print(f"Deleting all data for user: {user}")

# delete_user_data("admin")   # Output: Deleting all data for user: admin
# delete_user_data("guest")   # Output: Unauthorized access


# def authorized(fxn):
#     def inner_function(*args,**kwargs):
#         # print(args)
#         if args[0]=='admin':
#             fxn(*args,**kwargs)
#         else:
#             print('unauthorized access')
        
#     return inner_function

# @authorized
# def delete_user_data(user):
#     print(f'Deleting all data for user: {user}')
    
# delete_user_data('admin')
# delete_user_data('guest')




# a=input('enter the first part of 1stcomplex number')       #5+2i

# b=input('enter the second part of 1st(i) complex number')  #3+3i

# c=input('enter the first part of 2nd complex number')

# d=('enter the second part of 2nd(i) complex number')

# add= (a+c) +(b+d('i'))
# print(add)


# # class Add:
    
# #     def sum(self,x,y):
# #         self.x=x
# #         self.y=y
        










# def outer_function(fx1):
    
#     def inner_function():
#         print('Good Morning')
#         fx1()                         # Hello Brother
#         print('Good bye')    
        
#     return inner_function
    
# @outer_function

# def normal_function():
#     print('Hello Brother')
    
# normal_function()






# import time

# def outer_function(fx1):
    
#     def inner_function():
        
#         print('Good Morning')
#         fx1()                         # Hello Brother
#         print('Good bye')    
        
#     return inner_function
    
    
# def normal_function():
#     print('Hello Brother')
    
# return_func=outer_function(normal_function)
# return_func()



# ''' Using Show Method'''
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
        
#     def add(self,other):
#         real=self.real+other.real
#         img=self.img+other.img
#         return Complex(real,img)
    
#     def show(self):
#         print(f'{self.real}+{self.img}i')
        
# c1=Complex(2,4)
# c2=Complex(3,4)

# c3=c1.add(c2)
# c3.show()


# ''' Using __str__method'''

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
        
#     # def add(self,other):
#     #     real=self.real+other.real
#     #     img=self.img+other.img
#     #     return Complex(real,img)
    
#     def __add__(self,other):          # This allows direct sum for eg c3=c1+c2
#         real=self.real+other.real
#         img=self.img+other.img
#         return Complex(real,img)
    
    
#     def __str__(self):
#         return f'{self.real}+{self.img}i'
        
# c1=Complex(2,4)
# c2=Complex(3,4)
# c3=c1+c2
# # c3=c1.add(c2)
# print(c3)


# Task 
# Write a Python program that finds and prints the index of a given character in a predefined list. If the character is not present, print "Character not found." # mylist = ['a','b','c','d','e','f','g','h','i','j']

# mylist = ['a','b','c','d','e','f','g','h','i','j']

# char=input('enter any character ')



    
# if char in mylist:
#     print(f'index is',mylist.index(char))  
          
# else:
#     print('character not found')


# Write a Python program to categorize a person's age as "Child(0-12)," "Teenager(13-19)," 
# "Adult(20-64)," or "Senior(65 years and above)" and print the category.


# age=int(input('enter the age'))

# if  age<13:
#     print('the person is a child')
    
# elif age>12 and age<20:
#     print('the person is teeanger')
    
# elif age>19 and age<64:
#     print('the person is Adult')

# else:
#     print('the person is senior')


# mylist = [1,2,3,4,5,6,7,8,9,10]
# mytuple = (1,2,3,4,5,6,7,8,9,10)
# myset = {1,2,3,4,5,6,7,8,9,10}
# mydictionary = {1:1,2:4,3:9,4:16,5:25}


# mylist= list(x for x in range(1,11))
# print(mylist)

# mytuple= tuple(x for x in range(1,11))
# print(mytuple)

# myset= set(x for x in range(1,11))
# print(myset)

# mydictionary=dict{x:x*x for x in range(1,5)}
# print(mydictionary)
    


# mylist=[]

# for i in range(1,11):
#     mylist.append(i)
# print(mylist)

        

# mylist = [1,2,3,4,5,6,7,8,9,10]
# new_list = []

# for i in mylist:
#     if i%2==0:
#         new_list=new_list+[i]
        
# print(new_list)

# mytuple = (1,2,3,4,5,6,7,8,9,10)
# new_tuple = ()

# for i in mytuple:
#     if i%2!=0:
#         new_tuple=new_tuple+(i,)
        
# print(new_tuple)


# myset = {1,2,3,4,5,6,7,8,9,10}
# new_set = set() #{2,3,5,7}

# for i in myset:
#     if i!=1:
#         if i%i==1 and i%1==i:
#             new_set.add(i)
    
# print(new_set)

# mydictionary = {'a':500,'b':200,'c':300,'d':400,'e':50}
# value > 300

# new_dictionary = {}

# for i,v in mydictionary.items():
#     if v>300:
#         new_dictionary[i]=v
# print(new_dictionary)




'''

# WAPP to take a sentence and then prints the number of words in that sentence. 
 
# WAPP that takes a string as input and counts the number of vowel letters in it. 
'''

# WAPP that checks if a string is a palindrome. 

# word=input('enter a string')

# if word == word[::-1]:
#     print('palindrome')
# else:
#     print('not palindrome')
    
    

# WAPP that takes a string as input and counts the number of uppercase letters in the string. 
# word=input('enter any string ')
# for i in word:
#     if i is Upper():
#         count=0
#         count=count+1
# print(count)


# WAPP that takes a string as input and counts the number of vowel letters in it.

# word=input('enter a string ')

# for i in word:
#     # print(i)
#     if i == 'a' or 'e' or 'i'or 'o' or 'u':
#         count=0
#         count=count+1
    
# print(count)
            
            
# WAPP to take a sentence and then prints the number of words in that sentence.

# sentence=input('enter a sentence ')

# for i in sentence:
#     # print(i)
#     if i!=' ':
#         i=i+1
#     elif i==' ':
#         count=0
#         count=count+1
#         i=i+1
#     elif i==' '' ':
#         break
        
# print(count)

# hello good morning


# Generate a list of numbers from 1 to 10 using for loop and list comprehension. 
# Given a list, return a new_list with only the even numbers. Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# mylist=[1,2,3,4,5,6,7,8,9,10]
# new_list=filter(lambda x:x%2==0,mylist)
# print('Filter',list(new_list))





# Find the second largest element in a list. Input: [10, 20, 5, 7, 3]

# mylist=[10,20,5,7,3]

# print(max(mylist))





# Remove duplicates from a list. Input: [1, 2, 2, 3, 4, 4, 5]

# mylist=[1, 2, 2, 3, 4, 4, 5]

# for i in mylist:
#     if i==i:
#         i=2-i
#     else:
#         pass


        

# # Write a program to count the occurrences of each element in a list. Input: [1, 2, 2, 3, 4, 4, 4]

# mylist=[1, 2, 2, 3, 4, 4, 4]

# for i in mylist:
#     if i==1:
#         count=0
#         count=count+1
#         i=i+1
#         print('count of 1 is ',count)
        
#     elif i==i:
#         count=0
#         count=count+1
#         i=i+1
#         print('count of 2',count)
        
#     elif i==i:
#         count=0
#         count=count+1
#         print('count of 3',count)
        
#     elif i==i:
#         count=0
#         count=count+1
#         print('count of 4',count)
        
#     else:
#         pass


# Given the tuple t = (1, 2, 3, 2, 4, 2, 5), write code to
# find how many times the number 2 appears and its first index.


# tuple=(1,2,3,2,4,2,5)

# print('the number of occurence of 2',tuple.count(2))
# print('the index of ifrst 2',tuple.index(2))

# count=0
# index=0
# for i in tuple:
#     if i==2:
        
#         count=count+1 
        
# print(count)

# Create a set, add an element to it, and then remove an element. 
# Print the set after each operation.

# myset=set()


# if len(myset)==0:
#     myset.add('a')
#     myset.add('b')
# print(myset)


# if len(myset)!=0:
#     myset.remove('a')
    
# print(myset)
        

#built in exception
# Userdefined Exception

# Try block contains code which may cause exceptions
#  syntax

# try:
    # statements
    
#except exceptionname:
#   statements

#else block
#Finally block


'''
-> with the exception class name

except exceptionclassname:
    statement
    
->exception as an object
except exceptionclassname as obj:
    statement
    
-> Multiple Exception within tuple

except (exceptionclassname1,exceptionclassname2)

-> except

'''

'''
a=10
b=0
try:
    d=a/g
    print(d)
    # print('inside try')
# except ZeroDivisionError as obj:
#     print(obj)
    
# except NameError as ob:
#     print(ob)

# except(NameError,ZeroDivisionError) as obj:
#     print(obj)

except:
    print('exception handler')
    
# else:
#     print('inside else')
    
# finally:
    # print('inside finally block')
print('rest of the code')

'''
'''
class BalanceException(Exception):
    pass

def checkbalance():
    money=10000
    withdraw=9000
    try:
        balance=money-withdraw
        if(balance<=2000):
            raise BalanceException('insufficent balance')
        print(balance)
    except BalanceException as be:
        print(be)
    
checkbalance()


'''





# Write a program that tries to print the value of a variable named x. 
# If x is not defined handle possible error. (NameError)
#aadish 1
# try:
#     print(x)
    
# except NameError:
#     print('Name error')

# else:
#     print(x)


# Write a program that takes two string and attempts to concatenate them. Handle possible error.(TypeError)

#aadish2
# try:
#     word1=input('enter any word')
#     word2=input('enter any word')
    
# except TypeError:
#     print('Type error')
    
# else:
#     print(word1+word2)
# finally:
#     print('execution successfull')
    
#aadish2
# try:
#     x=int(input('enter any integer'))
#     y=int(input('enter any integer'))
    
# except ValueError:
#     print('Value error')
    
# else:
#     print(x+y)
# finally:
#     print('execution successfull')

# Create a program that defines a list of five elements and tries to access the sixth element. 
# Handle possible error. (IndexError)

# aadish3
# mylist=[1,2,3,4,5]

# try:
#     print(mylist[8])
    
# except IndexError:
#     print('index error')
    
# else:
#     print(mylist)

# finally:
#     print('execution successfull')
    
# Write a program that defines a dictionary with three key-value pairs.
# Attempt to access a key that does not exist in the dictionary. Handle possible error. (KeyError)

#aadish4
# mydict={'a':100,'b':200,'c':300}

# try:
#     print(mydict['e'])
    
# except KeyError:
#     print('Key Error')
    
# else:
#     print(mydict)
    
# finally:
#     print('execution sucessfull')

# Create a function that takes two numbers as input and returns their division. 
# Handle possible exception. (ZeroDivisionError)

#aadish5
# try:
#     a=int(input('enter any number '))
#     b=int(input('enter any number '))
    
# except ZeroDivisionError:
#     print('enter any number except zero')
    
# else:
#     c=a/b
#     print(c)
    
# finally:
#     print('Execution successfull')
    

# Write a python program to append an item to a tuple using append() method. 
# Handle possible exception. 

#aadish6
# mytuple=(1,2,3,4)
# try:
#     mytuple.append(8)
    
# except AttributeError:
#     print('Attribute Error')
    
# else:
#     print('there is no append method in tuple')
    
# finally:
#     print('Execution Sucessfull')
    
# Create a program that tries to import a xyz module that does not exist. 
# Handle possible error.

#aadish7
# try:
#     import ABC
# except ModuleNotFoundError:
#     print('Module not found')
    
# else:
#     print('module imported successfully')

# finally:
#     print('Execution successfull')



# file=open('example.txt','r')
# # content=file.read()    #read entire content
# line=file.readline()     #read one line at a time
# lines=file.readlines()    #reads file into list
# print(lines)
# # print(content)

# file.close()

# try:
#     file = open('example.txt', 'r')
#     print("File opened successfully.")
# except FileNotFoundError:
#     print("File not found.")
# except IOError:
#     print("An error occurred trying to open the file.")
# finally:
#     file.close()  # Don't forget to close the file

# try:
#     file = open('example.txt', 'r')
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print('File not found, please check the path or filename.')
# finally:
#     file.close()


# file = open('hello', 'w')
# file.write('Hello, World!')
# lines=['line 1\n','line 2\n']
# file.writelines(lines)
# file.close()


# file = open('hello', 'a')
# file.write('This line is added to the file.')
# file.close()





# with open('ticket.png', 'rb') as file:
#     binary_data = file.read()
#     print(binary_data)









# import os
# if os.path.exists('hello'):
#     os.remove('hello')
#     print('FILE DELETED')
# else:
#     print('file does not exist')

# if os.path.exists('example.txt'):
#     os.remove('example.txt')
#     print('File deleted.')
# else:
#     print('File does not exist.')


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in the local directory's users.db file.
engine = create_engine('sqlite:///users.db', echo=True)

# Declare a base for model classes
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

# Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
Base.metadata.create_all(engine)



