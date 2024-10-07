''' LIST OPERATION CONCATENATE, MULTIPLICATION ,IDENTIY,MEMBERSHIP'''

''' concatenation '''
list1=[1,2,4,[2,3]]
list2=[5,6,7,[8,9]]
list3=list1

print(list1 + list2)

''' multiply '''
print(list1*3)

''' identity '''
print(list3 is list1)      #True
print(list3 is not list2)  #True

''' membership '''
print(1 in list1)          #True
print([2,3] not in list1)  #False

