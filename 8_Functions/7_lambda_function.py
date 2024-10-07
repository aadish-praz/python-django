#lambda function
#lambda arguments:expression



''' Squaring using lambda function'''
# a= lambda x:x*x
# print(a(5))

# result= lambda x:x*x
# print(result(5))




''' Addition using lambda function'''
# a=lambda x,y:x+y
# print(a(3,4))


# result=lambda x,y:x+y
# print(result(3,4))



''' Higher Order Functions With lambda Function '''

''' Map With lambda function'''
mylist=[1,2,3,4,5]

    
result=map(lambda x:x*x,mylist)
print('Map',list(result))



''' Filter With lambda function '''

mylist=[1,2,3,4,5,6,7,8,9,10]


result=filter(lambda x:x%2==0,mylist)
print('Filter',list(result))




''' Reduce With lambda function '''

from functools import reduce
mylist=[1,2,3,4,5]


result=reduce(lambda x,y:x+y,mylist)
print('Reduce',result)

