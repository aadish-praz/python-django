# + 
x='hello'
y='world'
print(x+y)   #helloworld

# *
print(x*3)   #hellohellohello



# is, is not

# x='one'
# print(x is 'one')   #True
# print(x is not 'one')  #False

a='hello'
b='world'
c='hello'

print(a is c)      #true  (string is immutable so doesn't change in the memory location)
print(a is not b)  #true

#first check if the variable is mutable or immutable 
#if immutable then the identity operator returns True  because while creating another variable with same content, it first check the available variables and if already available it points to the same location else 
#if mutable then the identity operator returns False
 
# in, not in

x='Coding'
print('C' in x)      #True
print ('C' not in x) #False