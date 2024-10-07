# Strings are the immutable datatype in python. 
# They are sequence of characters enclosed inside single, double or triple quotes.

mystring = ''
mystring = ""
mystring = ''''''
mystring = str()
mystring = "H"
mystring = "Hello World"
mystring = "123"
mystring = "abcdefghijklmnopqrstuvwxyz"

#indexing and slicing
# print(mystring[0])   #a
# print(mystring[7])   #h
# print(mystring[18])  #s

# print(mystring[0:10])     #abcdefghij
# print(mystring[0:])       #abcdefghijklmnopqrstuvwxyz
# print(mystring[:10])      #abcdefghij
# print(mystring[0:27:2])   #acegikmoqsuwy
# print(mystring[19:9])     # error: we can't go from right to left

# print(mystring[-1])      # z
# print(mystring[-17])     # j
# print(mystring[-9])      # r

# print(mystring[-20:-25])    # error
# print(mystring[::-1])       # reverse  z...a
# print(mystring[-3:-10:-1])  #x w v u t s r 




# what are strings in python?How are strings represented in python?Examples?

'''
  ->Strings are the immutable datatypes in the python . 
    Strings are represented as ' '," " 
    for eg a='john',b="jimmy"
'''

# What is the result of the following indexing operations?
# mystring="abcdefghijklmnopqrstuvwxyz"

'''
  -> a
  -> h
  -> s
'''

# What is the result of the following slicing operations?
# mystring="abcdefghijklmnopqrstuvwxyz"

'''
  -> a....j
  -> a...z
  -> a,c,e,g,i,k,m,o,q,s,u,w,y
  -> gives blank
'''

# What is the result of the following negative indexing operations?
# mystring="abcdefghijklmnopqrstuvwxyz"

'''
  -> z
  -> j
  -> r
'''

# What is the result of the following reverse slicing operations?
# mystring="abcdefghijklmnopqrstuvwxyz"

'''
  ->gives blank
  -> z....a
  ->x,w,v,u,t,s
'''

# How do you find the index of a character in a string? Give an example?
'''
  We can find the index of a character in a string using mystring.index('character')
  for eg a='john'
   to find the index of j we can use print(mystring.index('j'))
'''

'''
  print(mystring.count('j'))
  
  print(mystring.replace('j','k'))
  
  print(mystring.strip())
  
  print(mystring.uppercase())
  
  print(mystring.lowercase())
  
  print(mystring.capitalize())
  
  print(mystring.title())
  
  print(mystring.startswith('a'))
  
  print(mystring.endswith('z'))
  
  print(mystring.split())
  
  mylist=['apple','banana','cherry']
  
  print(' ',mystring.join(mylist))
  
  #print(' '.join(mylist))
  
'''

'''
  a='john'
  b='cena'
  
  print(a + b)  #john cena
  
  a='john'
  print(a*3)  # johnjohnjohn
  
  a='apple'
  b='banana'
  c='apple'
  
  print(a is c)     #True
  print(a is not b) #True
  
  a='england'
  
  print('e' in a )   #True
  print('b' no in a) #True
'''

'''
language1='ram'
language2='prajapati'

#format()
print('my name is {language1} {language2}).format(language1,language2)

#f-strings
print(f'my name is {language1} {language2})
'''