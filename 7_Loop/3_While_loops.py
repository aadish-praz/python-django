# while
'''
string1 = "Happy Coding!!!"
index=0
while index<len(string1):
    print(string1[index])
    index +=1
'''
'''
list1 = ['a','b','c','d','e']
index=0
while index<len(list1):
    print(list1[index])
    index +=1
    
'''

'''
tuple1 = ('a','b','c','d','e')
index=0
while index<len(tuple1):
    print(tuple1[index])
    index +=1
'''
'''
set1 = {'a','b','c','d','e'}
list2=list(set1)
index=0
while index<len(list2):
    print(list2[index])
    index +=1
    
'''

dictionary1 = {'a':100,'b':200,'c':300,'d':400,'e':500}
items = list(dictionary1.items())  # Convert dictionary items to a list of tuples
index = 0

while index < len(items):
    key, value = items[index]
    print(f'{key}: {value}')
    index += 1
