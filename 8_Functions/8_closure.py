''' Nested Function '''

def out_func():
    # print('hello world')
    
    def in_func():
        print('hello world')
        
# in_func()   
# out_func()



''' Closure Function Examples'''

# def out_func(var):
#     def in_func():
#         print(var)
#     return in_func
    
# return_func=out_func('hello')
# return_func()


# def out_func(x):
#     def in_func(y):
#         return x+y
        
#     return in_func
    
# return_func=out_func(5)
# print(return_func(6))

# Task1: Create a closure function that multiplies a fixed number (say 3) by its input: 
# Task2: Create a closure function that checks if a given number is greater than a fixed threshold (say 10):



# def out_func(x):
#     def in_func(y):
#         return x*y
       
#     return in_func
    
# return_func=out_func(3)
# print(return_func(4))
# print(return_func(5))




# def out_func(x):
#     def in_func(y):
#         if y>x:
#             return True
#         else:
#             return False
        
#     return in_func
    
# return_func=out_func(10)
# print(return_func(5))


''' Closure Example 3   (Function passing)'''

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


# ''' Time Calculation Using Closure '''
# import time
# def outer_function(fx1):
    
#     def inner_function():
#         start_time=time.time()
#         fx1()                       
#         end_time=time.time() 
#         # time_taken=end_time-start_time
#         print('the time taken is',end_time-start_time)
        
#     return inner_function
    
    
# def normal_function():
#     for i in range(1,100000000):
#         pass
        
    
# result_func=outer_function(normal_function)
# result_func()





# def outer_func(func):
#     def inner_func(*args,**kwargs):
#         pw=input("Enter password: ")
#         if pw=="123":
#             func(*args,**kwargs)
#         else:
#             print()

#     return inner_func

# @outer_func
# def normal_func(x,y):
#     print("x + y = ",x+y)

# normal_func(3,4)


# def outer_func(fxn):
#     def inner_func(*args,**kwargs):
#         pw=input('enter password: ')
#         if pw=='123':
#             fxn(*args,**kwargs)
#         else:
#             print()
#     return inner_func

# @outer_func
# def normal_func(x,y):
#     print('x+y',x+y)
    
# normal_func(3,4)


# def outer_function(fxn):
#     def inner_function(*args,**kwargs):
#         pw=input('enter password')
#         if pw=='123':
#             fxn(*args,**kwargs)
#         else:
#             print('Invalid Password')
            
#     return inner_function

# @outer_function
# def normal_function(x,y):
#     print('x+y=',x+y)
    
# normal_function(3,4)


