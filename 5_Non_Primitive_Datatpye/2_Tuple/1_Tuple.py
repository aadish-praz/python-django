# Tuples
# Immutable datatypes
# Enclosed within small brackets
# Sequence of heterogeneous data types

# Creating an empty tuple
my_tuple = ()
my_tuple = tuple()

# Creating a tuple with a single element   !! Note : we can't use my_tuple=(1) it gives the integer value
my_tuple = (1,)

# Creating a tuple with multiple elements
my_tuple = (1,2,3,4,5)
mix_tuple = (1,2,3.1415,True,"Hello")
heterogeneous_tuple = (1,2,3.1415,True,"Hello",[4,5],(6,7),{8,9},{'a':"apple",'b':"banana"})

# Using tuple comprehension
tuple_comp = tuple(x for x in range(1,11))
#print(tuple(tuple_comp))
print(tuple_comp)

# Tuple packing and unpacking
my_tuple = 1,2,3,4,5
print(my_tuple)

a,b,c,d,e = my_tuple
print(a)   #1
print(b)   #2
print(c)   #3
print(d)   #4
print(e)   #5

# indexing and slicing
tuple3 = ('a','b','c','d','e','f','g','h','i','j')
print(tuple3[0])      #a
print(tuple3[0:5])    #'a','b','c','d','e'
print(tuple3[5:9])    #'f','g','h','i
print(tuple3[5:])     # 'f','g','h','i','j'
print(tuple3[:5])     # 'a','b','c','d','e'
print(tuple3[0:10:2])  # a,c,e,g,i
print(tuple3[8:3])      #empty tuple
 
print(tuple3[-1])       #j
print(tuple3[-8:-1])    #'c','d','e','f','g','h','i'
print(tuple3[-2:-8])    # empty tuple
print(tuple3[::-1])      #reverse
print(tuple3[-1:-8:-1])   # j,i,h,g,f,e,d

# Changing tuple item
'''
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
'''