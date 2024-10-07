# Types of Error
'''
1. Syntax Error
2. Runtime Error
3. Logical Error
'''


# Syntax Error
'''
These errors are identified during the compilation process or during the interpretation of the code

like

->example 1:
print hello world

->example 2:
if 10=10:
    print('the number is 10')
    
->example 3:
def myfunction()
    print('myfunction')
    
->example 4:
class='hello'

->example 5:
1var=10
'''


# Runtime Error
'''
Those error that are identified during the execution of program
->Runtime eroors are occured if there is not any suntax error.
->like zerodivisonerror,trying to used unassigned variable,unvailable attributes

like
1. Value Error

print(int('hello'))

2. Name Error

print(a)

3. Type Error
print(10+'hello')

4. Index Error
mylist=[1,2,3,4]
print(mylist[20])

5. Key Error
mydict={'a':100,'b':200}
print(mydict['z'])

6.Zerodivison error
print(10/0)

7.Attributes Error
mytuple(1,2,3,4,5)
mytuple.append(8)

8.Modulenot found error

import ABC
'''

# Logical Error
'''
Logical errors occurs when the program is syntatically correct and there is no any runtime error but
there is some mistake in the program that gives unexpected output due to the use of wrong logic or 
algorithm.

examples
->Example 1
a=10
b=6
average=a+b/2
print(average)

->Example 2
length =10
width =5
area =length - width
print (area)

->Example 3
total = 0
for i in range (1,5):
    total=total+i
print(total)

'''