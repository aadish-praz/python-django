'''
->JSON
->Javascript object Notation
->Json is a file extension use for the data communication between frontend and backend ,between backend and 
  backend.

->JSON is similar to Python dictionary having keys and values .Unlike python dictionary,keys of json
  must be string enclosed in double quotation marks .and values can be following data type

-> 


'''

'''
string: must be enclosed in double quotation
numbers : int,float
Boolean: true,false(similar to True and False in python)
Null:null(similar to None in python)
Array:[1,2,3,'hello',true](similar to list in python)
Object: similar to python dictionary
'''


#Example of python dictionary

py_student={
    
    'name':'ram',
    'age':20,
    'is_student':True,
    'phone':None,
    'course':['python','django','drf'],
    'address':{
        
        'city':'Bhaktapur',
        'country':'Nepal'
     } 
    
}

#Equivalent json object
json_string='''{
    
    "name":"ram",
    "age":20,
    "is_student":true,
    "phone":null,
    "course":["python","django","drf"],
    "address":{
        "city":"bhaktapur",
        "country":"Nepal"
    }
    
    
}'''


#Conversion of python dictionary to json string

# import json
# json_object=json.dumps(py_student)
# print(json_object)

#Conversion from JSON string to python dictionary

# import json
# py_dict=json.loads(json_string)
# print(py_dict)


#using file
#conversion from json string to python dictionary

# import json
# print('')
# with open('student.json','r') as file:
#     data=file.read()
    
# py_dict=json.loads(data)
# print(py_dict)


#Conversion from python dictionary to json file
import json
# print('')

# dictionary2={'id':1,'name':'alex','age':19,'address':'alaska'}

# json_string=json.dumps(dictionary2,indent=4)

# with open('student2.json','w') as file:
#     file.write(json_string)
    

# Using load and dump in file
# Conversion from json string to python dictionary

# import json
# with open('student.json','r') as file:
#     py_dict=json.load(file)
# print(py_dict)


#Conversion from python dictionary to json string

import json

dictionary2={'id':1,'name':'alex','age':19,'address':'alaska'}
with open('student2.json','w') as file:
    json.dump(dictionary2,file,indent=4)
