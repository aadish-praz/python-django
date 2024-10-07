my_tuple = ()
print(dir(my_tuple))

#Tuple being immutable there only two methods

# index
tuple1 = ('a','b','c','d','e')
print("\nIndex of c:", tuple1.index('c'))  #2

# count
tuple1 = ('a','b','c','d','e','e','e')
print("\nCount of e", tuple1.count('e'))   #3