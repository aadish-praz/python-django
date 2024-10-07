# 1.global,non_local

# Same Variable name inside and outside the function

# x=10

# def myfunction():
#     x=20
#     print(x)
    
# myfunction()
# print(x)
    

#gloabl Keyword

#Case 1

# x=10

# def myfunction():
#     global x
#     x=20
#     print(x)
    
# myfunction()
# print(x)

#Case 2

# x=10

# def outerfunction():
#     x=30
    
#     def innerfunction():
#         global x
#         x=20
#         print(x)
#     innerfunction()
#     print(x)   #20
        
# outerfunction()   #30
# print(x)   #20




#case 3  (Nonlocal)

x=10

def outerfunction():
    x=30
    
    def innerfunction():
        nonlocal x
        x=20
        print(x)
        
    innerfunction()   #20
    
    print(x)
outerfunction()      #20

print(x)     #10