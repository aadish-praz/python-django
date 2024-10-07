'''
     MEMBERSHIP AND IDENTIY OPERATIONS
'''

#dictionary1={'a':100,'b':200,'c':300,'d':400,'e':600}
# dictionary2={'a':100,'b':200,'c':300,'d':400,'e':600}
# dictionary3=dictionary1

# print(dictionary3 is  dictionary1)    # True
# print(dictionary1 is not dictionary2)  #True
# print(dictionary1 is dictionary2)     #false


''' can use if and else condition in membership and identity operation'''

# print('a' in dictionary1)     #true
# print('z' not in dictionary1)  #true
# print('b' not in dictionary2)   #false

#sum,all,any

dictionary1={'a':100,'b':200,'c':300,'d':400,'e':600}

result=sum(dictionary1.values())
print(result)

dictionary1={'a':100,'b':200,'c':0,'d':400,'e':600}
print(any(dictionary1.values()))   #OR

dictionary1={'a':100,'b':0,'c':300,'d':400,'e':600}
print(all(dictionary1.values()))   #And