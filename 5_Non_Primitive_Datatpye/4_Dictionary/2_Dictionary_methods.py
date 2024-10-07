# my_dict={}
# print(dir(my_dict))


'''
update
pop,popitem,clear

 '''
 
 
# dictionary1={'a':100,'b':200,'c':300,'d':400}
# dictionary2={'d':500,'e':600,'f':700}

# dictionary1.update(dictionary2)
# print(dictionary1)

# result=dictionary1.pop('a')
# print(dictionary1)
# print(result)

# result=dictionary1.popitem()
# print(dictionary1)
# print(result)

# dictionary1.clear()  #doesn't return value
# print(dictionary1)


'''
get,setdefault

'''

# dictionary1={'a':100,'b':200,'c':300,'d':400,'e':600}

# result=dictionary1.get('a')   # returns key value 
# print(result)
# result=dictionary1.get('z','random')
# print(dictionary1)   #no change in dictionary
# print(result)       # gives value of the key


# result=dictionary1.setdefault('e',500)   #if not present new key and values are added from set default
# result=dictionary1.setdefault('e',500)    #but if value is already present then it doesn't changes the value in dictionary
# print(dictionary1)     # e is added
# print(result)          # value of key e is shown

'''
items,keys,values
'''
#        #ITEMS
# dictionary1={'a':100,'b':200,'c':300,'d':400,'e':600}
# print(dictionary1.items())

# #        #KEYS
# dictionary1={'a':100,'b':200,'c':300,'d':400,'e':600}
# print(dictionary1.keys())
        
# #        #VALUES
# dictionary1={'a':100,'b':200,'c':300,'d':400,'e':600}
# print(dictionary1.values())

# for keys in dictionary1.keys():
#     print(keys)
    
# for keys,values in dictionary1.items():       #unpacking
#     print(keys,values)


'''
copy fromkeys


'''

dictionary1={'a':100,'b':200,'c':300,'d':400,'e':600}

dictionary2=dictionary1.copy()    #only use shallow copy in dictionary
print(dictionary2)

mylist=[1,2,3,4,5]
dictionary2=dict.fromkeys(mylist,'random')    #we can use list also to give from keys
#dictionary2=dict.fromkeys(dictionary1,'random')
print(dictionary2)