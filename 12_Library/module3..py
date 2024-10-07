#import package
# import mypackage
# print('')
# print(my_package.__version__)
# print(my_package.__author__)

''' 1 .from package import module '''

# from my_package import module1
# from my_package import module2

# print('')
# module1.addition()
# module2.addition()


''' 2 .from package.module import function '''

# from my_package.module1 import addition
# from my_package.module2 import addition

# print('')
# addition()   #the second function replaces the first function in the process so result is addition from 2


# from my_package.module1 import addition as add1
# from my_package.module2 import addition as add2

# print('')
# add1()
# add2()


'''3 . from init file '''

# import my_package
# print('')
# print(my_package.__version__)
# print(my_package.__author__)
# my_package.add1()
# my_package.add2()


## from package import function
# from my_package import add1
# from my_package import add2

# print('')
# add1()
# add2()


### from package import all
from my_package import *

print('')
add1()
add2()

print(__author__)
print(__version__)