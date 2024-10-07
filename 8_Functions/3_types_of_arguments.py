#Types of Argument in Function

'''
1. Positional Argument
2. Keyword Argument
3. Arbitary Argument(Postional,Keyword)
'''

# print('\n Positional Argument')
# def students(name,age,address):
#     print('Name: ',name)
#     print('Age: ',age)
#     print('Address: ',address)

# '''
# Note in postional argument the parameters must be passed on order if they are passed randomly it gives answer in the same order
# '''
# students('Ram',16,'Kathmandu')
# students(16,'ram','ktm')

# print('\n Keyword Argument')
# def students(name,age,address):
#     print('Name: ',name)
#     print('Age: ',age)
#     print('Address: ',address)
    
# '''
# key difference even if we passed parameters randomly it will show in order 
# '''
# students(name='adish',age=22,address='bkt')
# students(age='18',address='bkt',name='ram')

# print('\n Default Argument')
# def students(name,age,address='bkt'):
#     print('Name: ',name)
#     print('Age: ',age)
#     print('Address: ',address)
    
# students('adish',26)   #gives error since one parameter is missing if not used Default Argument
# students('adish',26)   #pass the default keyword in address

# print('\nArbitary(Positional)Argument')


# def students(*args):
#     print(args)
#     print('Name: ',args[0])
#     print('Age: ',args[1])
#     print('Address: ',args[2])
    
# students('adish',16,'bkt')
    
# print('\n Arbitary(keyword) Argument')

# def students(**kwargs):
#     print(kwargs)
#     print('Name: ',kwargs['Name'])
#     print('Age: ',kwargs['Age'])
#     print('Address: ',kwargs['Address'])
    
# students(Name='adish',Age=16,Address='bkt')


''' Tasks on Function Arguments '''

#Postional argument

#Write a function 'multiply(a,b)' that returns the product of two numbers. Call this function with positional arguments to multiply 6 and 7. 


# def multiply(a,b):
#     return a*b

# result=multiply(6,7)
# print(result)


#Write a function 'multiply(a,b)' that returns the product of two numbers. Call this function with positional arguments to multiply 6 and 7. 


# def multiply(a,b):
#     return a*b
# result=multiply(5,4)
# print(result)


#Write a function 'swap(z,y)' that swaps the values of two variables and prints them. Call this function with positional arguments. 

# def swap(z,y):
#     z,y=y,z
#     print('z: ',z)
#     print('y: ',y)
 
   

# swap(5,8)



# Keyword argument
# Write a function person_info(name, age, city) that prints a person's name, age, and city. Call this function using keyword arguments.

# def persons_info(name,age,city):
#     print('Name: ',name)
#     print('Age: ',age)
#     print('City: ',city)
    
# persons_info(name='ram',city='ktm',age=16)


# Default argument
# Write a function calculate_total(price, tax=0.05) that calculates the total price after tax. Call this function with and without the tax argument.

# def calculate_total(price,tax=0.05):
#     return price+price*tax

# print(calculate_total(200))
# print(calculate_total(200,0.25))

'''
# def calculate_total(price,tax=0.05):
#     return price+price*tax

# # result=calculate_total(200)
# result=calculate_total(200,0.25)
# print(result)

'''


# Arbitrary argument
# Write a function sum_numbers(*args) that returns the sum of all the numbers passed to it using sum(). Call this function with a varying number of arguments.

# def sum_numbers(*args):
#     return sum(args)
   
# print(sum_numbers(2,5,1,3,4,9))

# def sum_numbers(*args):
#     return sum(args)

# result=sum_numbers(5,5,5,5)
# print(result)




# Write a function sum_numbers(*args) that takes an arbitrary number of numeric arguments and returns their sum. Use a for loop to iterate over the arguments.

# def sum_numbers(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum
    # result = sum_numbers(1,4,2,6,3,7)
# print(result)


# def sum_numbers(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# print(sum_numbers(5,6,7,8))
        




# Write a function sum_kwargs_values(**kwargs) that returns the sum of all the numeric values passed as keyword arguments. Use a for loop to iterate over the keyword arguments.



''' 1st Method '''
# def sum_kwargs_values(**kwargs):
#     sum=0
#     for values in kwargs.values():
#         sum=sum+values
#     return sum
# result=sum_kwargs_values(a=1,b=2,c=3)
# print(result)



''' 2nd Method '''
# def sum_kwargs_values(**kwargs):
#     sum=0
#     for keys in kwargs.keys():
#         values=kwargs[keys]
#         sum=sum+values
#     return sum

# result=sum_kwargs_values(a=5,b=4,c=1)
# print(result)


''' 3rd Method '''
# def sum_kwargs_values(**kwargs):
#     sum=0
#     for key,value in kwargs.items():
#         sum=sum+value
#     return sum

# result=sum_kwargs_values(a=1,b=2,c=3)
# print(result)
    

# def sum_kwargs_values(**kwargs):
#     # print(kwargs)
#     sum=0
#     for value in kwargs.values():
#         sum=sum+value
#     return sum

# result=sum_kwargs_values(x=1,y=2,z=3,w=4)
# print(result)

#Order of Functional Argument

'''
Postiional -> Default -> Arbitary(Postional,Keyword)
'''


# def students(a,b,c,d=4,e=5):    # we can't put default argument infront of postional as it will give error 
# #def students(d=4,e=5,a,b,c):
#     print('a',a)
#     print('b',b)
#     print('c',c)
#     print('d',d)
#     print('e',e)
    
# students(1,2,3)


# def students(*args,**kwargs):    # In arbitary also it follows order like from postional then keyword
#     print(args)
#     print(kwargs)
    
# students('ram',16,'bhaktapur',mob_no=9861287720,gender='male')
