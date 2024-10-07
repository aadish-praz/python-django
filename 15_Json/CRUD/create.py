import json

def createuser():
    # id = int(input("Enter user id "))
    while True:
        try:
            id = int(input("Enter a user ID: "))
            if id <= 0:
                print("ID must be a positive integer. Please try again.")
                continue


            try:
                with open("user.json", "r") as file:
                    my_list = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                my_list = []


            if any(user['id'] == id for user in my_list):
                print("This ID is already in use. Please enter a unique ID.")
            else:
                break  
            
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    name = input("Enter user name ")
    
    try:
        age = int(input("Enter user age: "))
        if age <= 0:
            print("Age must be a positive integer.")
            return
    except ValueError:
        print("Invalid age, Please enter a number.")
        return
    
    
    # age = int(input("Enter user age "))
    
    
    address = input("Enter user address ")

    my_dictionary = {"id":id,"name":name,"age":age,"address":address}

    try:
        with open("user.json","r") as file:
            my_list = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        my_list = []
        
    
    with open("user.json","w") as file:
        my_list.append(my_dictionary)
        json.dump(my_list,file,indent=4)