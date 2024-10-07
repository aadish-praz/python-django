# globals():
'''Function that returns the current global namespace as a dictionary. '''

# locals():
'''Function that returns the current local namespace as a dictionary. '''

# Namespace : 
'''
A namespace in python is a collection of names (identifiers like variable, functions etc) and their corresponding objects. 
Python implements namespaces as dictionaries, where the names are keys and the objects thery refer to are values. 
Namespaces allow the same name to be used in different scopes like modules, functions, or classes without conflicts.
'''

# Types of Namespaces
'''
1. Local namespace 
2. Enclosed namespace 
3. Global namespace 
4. Built-in namespace 
'''

# Scope
'''
A scope determines which namespace will be looked in and in what order. 

The order is define by LEGB rule. 
Local → Enclosed → Global → Built-in

L (Local): First, it looks in the local namespace of the current function.
E (Enclosing): If not found locally, it looks in the enclosing function's namespace (for nested functions).
G (Global): Then, it looks in the global namespace of the module.
B (Built-in): Finally, it checks the built-in namespace (e.g., len(), print()).

'''

# 1.Local namespace 
'''
Those namespaces which are created inside a fuctions.
Scope: Variables declared inside a function are accessible only within that function and cannot be accessed from outside.
'''

# Exmaple
def my_function():
    # local namespace
    x = 10
    print(x)
    # print(locals()) #{'x': 10}
my_function()

# def my_function():
#     x=10
#     print(x)
#     #print(locals())
# my_function()

#print(x) # not accessible

# 2.Enclosing namespace
'''
Enclosing namespaces are created inside outer function when you have nested inner function within the outer function. 
Scope: Variables in the outer function (enclosing function) are accessible to the inner function but not outside the outer function.
'''

# Exmaple
def outer_function():
    # Enclosing namespace
    x = "10"
    # print(locals()) # {'x': 10}

    def inner_function():
        # print(locals()) # {'x': 10}
        print(x) # Inner fxn can access enclosing_var

    inner_function()

outer_function()
#print(x) # Not accessible

# def outer_function():
#     x=10
    
#     def inner_function():
#         print(x)
#     inner_function()
    
# outer_function()
# print(x)

# 3.Global namespace
'''
Global namespace are created at the module level. 
Scope: Variables defined at the module level have a global scope, accessible anywhere within the module.
'''

# Exmaple
x = 10

def outer_function():
    print(x)

    def inner_function():
        print(x) 

    inner_function()

outer_function()
print(x) 
# print(globals()) #  'x': 10


# def outer_fxn():
#     print(x)
    
# def inner_fxn():
#     print(x)
    
# inner_fxn()
# outer_fxn()
# print(x)

# 4.Built-in namespace 
'''
The built-in namespaces are created when the Python interpreter starts, and are availabe through out the program execution. 
Scope: Built-in objects are accessible from any part of the code within needing to import them. 
'''

print("Hello World!!!")
print(dir(__builtins__))

