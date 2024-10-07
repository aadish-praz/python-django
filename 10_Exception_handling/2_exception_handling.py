# Exception Handling
'''
In order to handle the runtime error gracefully we use exception handling

'''

try:
    pass   # possible error ,exception
except:
    pass    # if exception occur
else:
    pass    # if there is no exception
finally:
    pass    # always execute


#Variation 1:

try:
    a=int(input('enter any value for a'))
    b=int(input('enter any value for b'))
    
except:
    print('please enter an interger value')
    
else:
    sum=a+b

finally:
    print('Execution sucessful')
    
    
#Variation 2:

try:
    a=int(input('enter any value for a'))
    b=int(input('enter any value for b'))
    
except Exception as e:
    print(e)
    print('please enter integer value')
else:
    sum=a+b

finally:
    print('Execution sucessful')
    
#Variation 3:

try:
    a=int(input('enter any value for a'))
    b=int(input('enter any value for b'))
    
except ValueError:
    print('please enter integer value')
else:
    sum=a+b

finally:
    print('Execution sucessful')
    
#Variation 4:

try:
    a=int(input('enter any value for a'))
    b=int(input('enter any value for b'))
    
except ValueError:
    print('please enter integer value')
    
except NameError:
    print('please assign the variable')
    
except TypeError:
    print('type mismatch')
else:
    sum=a+b

finally:
    print('Execution sucessful')
    
    
# Variation 5   
try:
    a=int(input('enter any value for a'))
    b=int(input('enter any value for b'))
    
except (ValueError,NameError,TypeError):
    print('Name Error or Value Error or Type Error')
    

else:
    sum=a+b

finally:
    print('Execution sucessful')