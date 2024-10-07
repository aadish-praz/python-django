# + Concatenation
print("\nTuple concatenation")
tuple1 = ('a','b','c','d','e')
tuple2 = ('d','e','f','g','h')
concatenated_tuple = tuple1 + tuple2 
print(concatenated_tuple)      #('a','b','c','d','e','d','e','f','g','h')

# * tuple repetition
print("\nTuple repetition")
tuple1 = (1,2,3,4,5)
repeated_tuple = tuple1 * 3
print(repeated_tuple)    #(1,2,3,4,5,1,2,3,4,5,1,2,3,4,5)

# is, is not
print("\nis, is not ")
tuple1 = ('a','b','c','d','e')
tuple2 = ('a','b','c','d','e')
print(tuple1 is tuple2) # True
print(tuple1 is not tuple2) # False

# in, not in
print("\nin, not in")
tuple1 = ('a','b','c','d','e')
print('a' in tuple1)       #True
print('z' not in tuple1)    #False