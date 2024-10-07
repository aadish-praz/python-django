# What are Operators?
# What are the types of Operator?
# Perform all the Arithmetic operations when x=5 and y=2 using Python.
# Perform all the Relational Operations when x=3 and y=2 using python.
# Give an example of a python logical operator(and,or,not)
# Give an example of a python bitwise Operator(&,|).
# Give an example of a python membership operator?(in,not in)
# Give an example of a python identity operator(is,is not).Compared with '==' and != operators

'''
-> Operators are s on which the operations are perfomred they may be arthmetic ,relational or operational.

-> types : Arithmetic, Relational , Logical , Bitwise, assignment, membership, identity

'''

# Arithmetic Operators
x=5
y=2
 #multiplication
print(x*y)

#Divison
print(x/y)

#Floordivison
print(x//y)

#Addition
print(x+y)

#Subtraction
print(x-y)


# Relational operator
x=3
y=5

if (x>=y):
    print('x is greater')
else:
    print('x is smaller')

if(x<=y):
    print('x is less than than y')
else:
    print('y is small or equal to y')#(less than or equal)
    

if(x!=y):
    print('x is not equal to y')#(is not equal to )
else:
    print('x is equal to y')


# Logical operator
x=3
y=2
   
print(x<10 and y<10)  #and operation gives result 2
print(x<10 or y<5)   #or operation gives result 3
    
   
# Bitwise
z=(x & y)    #result 2
print(z)
z=(x | y)    #result 3
print(z)



#Membership operator
x=('apple','banana','orange','pineapple')
if 'cherry' in x:
    print('true')
else:
    print('false')
        

x=('apple','banana','orange','pineapple')
if 'cherry' not in x:
    print('true')
else:
    print('false')
    
x = ["apple","banana"]
y = ["apple","banana"]
z   = x

# Identity
print(x is z)  #returns true as a and x are same memory location a is refrencing x
print(y is z)  # returns true since z and x are same content but different memory location
   
print(x==z)        #  it checks if the content of the x and z are same or not
print(y==z)        # it checks if the content of x and z are same or not
