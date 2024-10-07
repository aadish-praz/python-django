#File handling in python
#Basic three modes
'''
read mode (r)
write mode (w)
append mode (a)
'''

#read mode (r)
# print("read()")
# file=open("task/readtext.txt",'r')
# print(file.read())
# file.close()

# print("\nread(value)")
# file=open("task/readtext.txt",'r')
# print(file.read(5))
# file.close

# print("\nreadline()")
# file=open("task/readtext.txt",'r')
# print(file.readline())
# file.close()

# print("\nreadlines()")
# file=open("task/readtext.txt",'r')
# print(file.readlines()) #list of lines
# file.close()

# file=open("task/readtext.txt",'r')
# lines=file.readlines()
# for line in lines:
#     print(line.strip())
# file.close()

#write mode (w)
# file=open("task/writetext.txt",'w')
# file.write("Hello World!!")
# file.close()

# mylist=['a','b','c','d','e','f','g','h','i']
# file=open("task/writetext.txt",'w')
# file.writelines(mylist)
# file.close()

# #append mode (a)
# file=open("task/appendtext.txt",'a')
# file.write("Appending text to a file....")
# file.close