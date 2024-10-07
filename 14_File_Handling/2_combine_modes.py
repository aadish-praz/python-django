#combine modes
'''
read and write mode (r+)
write and read mode (w+)
append and read mode (a+)
'''

# Context manager with combine modes
with open("task/readtext.txt","r+") as file:
    data=file.read()
    print(data)
    file.write("\nThis is sixth line.")
    file.seek(0)
    print(file.read())

with open("task/readtext.txt","r+") as file:
    print(file.read(5))

with open("task/readtext.txt","r+") as file:
    print(file.readline())

with open("task/readtext.txt","r+") as file:
    lines=file.readlines()

for line in lines:
    print(line.strip())

# write and read mode (w+)
with open("task/writetext.txt",'w+') as file:
    file.write("Hello World!!!")
    file.seek(0)
    print(file.read())

mylist=['a','b','c','d','e','f','g','h','i']
with open("task/writetext.txt","w+") as file:
    file.writelines(mylist)
    file.seek(0)
    print(file.read())

# append and read mode (a+)
with open("task/appendtext.txt","a+") as file:
    file.write("\nAppending text to file....")
    file.seek(0)
    print(file.read())

