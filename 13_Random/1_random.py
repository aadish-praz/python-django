#random
import random

# print(dir(random))

'''
randint()
randrange()

random()
uniform()

choice()
choices()
sample()
shuffle()
'''

#randint()
# print(random.randint(1,20)) #randint(a,b) prints random integer from a to b including a and b

#randrange()
# for i in range(1,20):
#     print(random.randrange(1,20,2)) # can use steps will generate random odd numbers
    


# #random()
# for i in range(1,20):
#     print(random.random()) # generate random floating point values between 0 and 1

# #uniform()
# for i in range(1,20):
#     print(random.uniform(1,20)) #generate random floating point values between a and b for (a,b)

# #choice()
mylist=['a','b','c','d','e','f','g','h','i']
# for i in range(1,20):
#     print(random.choice(mylist)) #generate random values from given list



#choices()
# for i in range(1,20):
#     print(random.choices(mylist,k=5)) #values are repeated in the list

# #sample()
# for i in range(1,20):
#     print(random.sample(mylist,k=5)) # values are unique

# #shuffle()
random.shuffle(mylist) #shuffles the value inside the list
print(mylist)