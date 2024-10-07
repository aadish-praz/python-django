import random

# WAPP that generates a list of 10 random integers between 1 and 50 (inclusive).

# mylist=[]
# for i in range(10):
#     mylist.append(random.randint(1,50))
# print(mylist)


# WAPP that generates a list of 10 random numbers between 1 and 500 that are divisible by 5. 

# mylist=[]
# for i in range(10):
#     mylist.append(random.randrange(0,500,5))
# print(mylist)


# WAPP that generates a dictionary (weather_data) containing random weather data between 0 to 1 for the given list of keys.

# keys = ['temperature', 'humidity', 'wind_speed', 'precipitation', 'visibility']
# mydict={}
# for i in keys:
#     mydict[i]=random.random()
# print(mydict)



# Given a list of students ["Jon", "Jane", "Hary", "Alex","evan"], 
# create a list of dictionaries with random exam marks (float value between 1 to 100) 
# and random address from the list of given addresses. Print the address and marks of "Hary". 
# addresses = ["KTM", "Pokhara", "Bhaktapur", "Lalitpur","Mustang","Lumbini","Jumla","Illam"]
# addresses = ["KTM", "Pokhara", "Bhaktapur", "Lalitpur","Mustang","Lumbini","Jumla","Illam"]
# students=["Jon", "Jane", "Hary", "Alex","evan"]
# mydict={}
# mylist=[]
# print(dir(mylist))
# for i in students:
    # mydict={}
    # mydict['name']=i
    # mydict['address']=random.choice(addresses)
    # mydict['marks']=random.uniform(1,100)
    # mylist.append(mydict) # or mydict.copy()
    
    
# print(dir(mydict))
# print(mylist)
# for i in range(len(students)):
#     if mylist[i]['name']=='Hary':
#         print(mylist[i])

# Write a Python program that generates random lists of numbers from a predefined list. 
# The program should ask the user how many random lists they want to generate. 
# For each list, it should randomly determine the length and allow for repeated numbers in the generated lists.
# given_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# given_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# n=int(input("Enter no. of lists to be generated:"))

# for i in range(n):
#     print(random.choices(given_list,k=random.randint(1,len(given_list))))


