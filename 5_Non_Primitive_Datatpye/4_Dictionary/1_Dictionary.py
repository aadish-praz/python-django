# DICTIONARY
# Mutable data types ,{ }
# Keys are immutable while values can be mutuable

my_dict={}
print(type(my_dict))

dictionary={'a':100,'b':200,'c':300,'d':400}
print(dictionary)

#using constructor
dictionary=dict()
dictionary=dict([('a',100),('b',200),('c',300)])
print(dictionary)

#another method
dictionary=dict(a='john',b='ram',c='shyam')
print(dictionary)



dictionary={'a':100,'b':200,'c':300,'d':400}
print(dictionary['c'])

dictionary['b']=500   #change value
print(dictionary)

dictionary['z']=400    # insert
print(dictionary)

dictionary1={'name':'ram','age':10,'roll_No':4}
dictionary2={
    100:{'name':'Hari','age':12,'roll_no':10},
    101:{'name':'shyam','age':14,'roll_no':11},
    102:{'name':'sita','age':15,'roll_no':11},
    103:{'name':'gita','age':16,'roll_no':12}
    
}

print(dictionary2[102]['age'])


''' Zip function Example'''
# keys=['a','b','c','d','e','f']
# values=[1,2,3,4,5,6]
# mydict=zip(keys,values)
# print(dict(mydict))