
""" LIST METHODS"""

''' index,count,append,insert,extend'''
list0=['a','b','c','d','d']
list1=['d','e','f','g']

print(list0.index('a'))
print(list0.count('d'))

# list0.append('e')
# print(list0)

# list0.insert(1,['x','y'])
# print(list0)

# list0.extend(list1)
# print(list0)

 
'''pop remove clear'''
 
# list0=['a','b','c','d','e']

# result=list0.pop(1)
# print(list0)
# print(result)

# list0.remove('a')
# print(list0)

# list0.clear()
# print(list0)

''' reverse ,sort'''

# list0=['a','b','e','f','e']

# list0.reverse()
# print(list0)

# list0.sort()
# print(list0)

''' copy {Assignment copy, shallow copy, Deep copy}'''


# from copy import deepcopy

# list=['a','b','e','f','e',[1,2,3]]

# assign_copy=list
# shallow_copy=list.copy()
# deep_copy=deepcopy(list)



# #list[1]='c'
# list[5][1]=11


# print(assign_copy)
# print(shallow_copy)
# print(deep_copy)

# print(id(list))
# print(id(assign_copy))
# print(id(shallow_copy))
# print(id(deep_copy))
