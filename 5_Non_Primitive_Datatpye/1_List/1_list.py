# list 
# mutable datatypes 
# enclosed within square brackets []
# elements can be of heterogeneous datatypes

# mylist = []
# print("\nCreating empty list")
# print(mylist) # []

# mylist = list()
# print("\nCreating empty list using list constructor")
# print(mylist) # []

# mylist = [1,2,3,4,5]
# print("\nCreating a list with elements")
# print(mylist) # [1,2,3,4,5]

# mixed_list = [1,"hello",True,3.14]
# print("\nCreating a list with different types of elements")
# print(mixed_list) # [1,"hello",True,3.14]
 
# nested_list = [[1,2,3],[4,5,6],[7,8,9]]
# print("\nCreating a nested list")
# print(nested_list)

# num = [x for x in range(1,11)]
# print("\nCreating a list using list comprehension")
# print(num)

# print("\nIndexing and Slicing")
# #       ['0','1','2','3','4','5','6','7','8','9']
# list3 = ['a','b','c','d','e','f','g','h','i','j']


''' REPLACING LIST ITEMS '''

list=['apple','banana','mango','cherry','orange']

# list[2]='grapes'
# print(list)

# list[2:4]='litchi'
# print(list)

list[2:4]=['litchi'] 
print(list)
list[2:4]=['litchi','lemon','strawberry']  #while replacing in list it must be always in list not string.
print(list)

# print(list3[0]) #a
# print(list3[0:5]) #['a','b','c','d','e']
# print(list3[5:9]) #'[f','g','h','i']
# print(list3[5:]) #['f','g','h','i','j']
# print(list3[:5]) #['a','b','c','d','e']
# print(list3[0:10:2]) #['a','c','e','g','i']
# print(list3[8:3]) #[]

# print(list3[-1]) #j
# print(list3[-8:-1]) #['c','d','e','f','g','h','i']
# print(list3[-2:-8]) #[]
# print(list3[::-1]) #[j i h g f e d c b a]
# print(list3[-1:-8:-1]) # [j i h g f e d]