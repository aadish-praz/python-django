''' loop '''

''' Using String '''

# mystring='johnny'

#  #direct method
# for i in mystring:
#     print(i)
    
    #using range
# for i in range(len(mystring)):
#     print(i,mystring[i])

    #using enumerate
# for i,v in enumerate(mystring):
#     # print(i)
#     print(i,v)
    
''' For List'''

# mylist=['r','a','m','a']
#  #direct method
# for i in mylist:
#     print(i)
    
    #using range
# for i in range(len(mylist)):
#      print(i,mylist[i])

    #using enumerate
# for i,v in enumerate(mylist):     
#     # print(i)                        #print index and values in form of the tuple like (0,'r')
#     print(i,v)                        #prints both index and values  like 0 r
    
''' For Tuple '''    
    
# mytuple=('r','a','m','a','y','a','n')
#  #direct method
# for i in mytuple:
#     print(i)
    
    #using range
# for i in range(len(mytuple)):
#      print(i,mytuple[i])

    #using enumerate
# for i,v in enumerate(mytuple):
#     # print(i)
#     print(i,v)

''' Using Set '''

# myset={'r','a','m'}
#  #direct method
# for i in myset:
#     print(i)
    
#     '''using range'''
# # for i in range(len(myset)):    #gives error since range can't be used in set as it is unordered
# #      print(i,myset[i])       

# '''using enumerate'''
# for i,v in enumerate(myset):
#     # print(i)
#     print(i,v)
    
''' Using Dictionary '''

 #direct method
 
mydict={'a':100,'b':200,'c':300}
# for i in mydict:
#     # print(i)           # this will only print keys
#     print(i,mydict[i])   #this gives both keys and values
    
# for i in mydict.keys():
#     print(i)
    
# for i in mydict.values():
#     print(i)

# for i in mydict.items():
#     print(i)
    
'''using range'''
# for i in range(len(mydict)):    #gives error since range can't be used in set and dictionary 
#      print(i,mydict[i])       


''' using Enumerate '''

# for i,items in enumerate(mydict.items()):
#     print(i,items)
#     # print(i,v)
    
# for i,(k,v) in enumerate(mydict.items()):
#     print(i,k,v)


''' LIST COMPREHESION '''

# output=[1,2,3,4,5,6,7,8,9,10]
# mylist=[x for x in range(1,11)]
# print(mylist)

# output=[1,4,9,16,25]
# mylist=[x*x for x in range(1,6)]
# print(mylist)

# output=[2,4,6,8,10]
# mylist=[x+x for x in range(1,6)]
# print(mylist)

''' Dictionary Comprehesion '''

# output={1:1,2:2,3:3,4:4}
# mydict={x:x for x in range(1,5)}
# print(mydict)

# output={1:1,2:4,3:9,4:16,5:25}
# mydict={x:x*x for x in range(1,6)}
# print(mydict)

# output={2:2,4:4,6:6,8:8}
# # mydict={x+x:x+x for x in range(1,5)}
# mydict={x:x for x in range(2,9,2)}           #Another Method
# mydict={x:x for x in range(1,9) if x%2==0}
# print(mydict)



