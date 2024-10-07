
#iterable
'''
    object that can be looped over  list , tuple,set,dictionary,string
    object that can appear on the right side of for-loop, for x in iterable
    object that has an __iter__ method which returns an iterator
    object capable of returning its members one at a time
'''

#iterator
'''
    object with a  __next__ method
    object with a state so that it remember where it is during iteration
'''


''' How Iterator Works'''
# # mylist=['a','b','c','d']
# mydict={'a':100,'b':200,'c':300}

# # iterator=iter(mylist)    #using iter() constructor
# iterator=iter(mydict)

# key = next(iterator)         #For Dictionary
# print(key,mydict[key])
# # print(next(iterator))      #Print Each Element
# # print(next(iterator))
# # print(next(iterator))



''' Backend process of for loop in python '''
mylist=['a','b','c','d']
mydict={'a':100,'b':200,'c':300}

# iterator=iter(mylist)
iterator=iter(mydict)
while True:
       try:
           print(next(iterator))      #For List
           element=next(iterator)      #For dictionary to print both key and values
           print(element,mydict[element])
        
       except StopIteration:
           break