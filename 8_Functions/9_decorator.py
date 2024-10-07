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


def authorized(fxn):
    def inner_function(*args,**kwargs):
        # print(args)
        if args[0]=='admin':
            fxn(*args,**kwargs)
        else:
            print('unauthorized access')
        
    return inner_function

@authorized
def delete_user_data(user):
    print(f'Deleting all data for user: {user}')
    
delete_user_data('admin')
delete_user_data('guest')




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







