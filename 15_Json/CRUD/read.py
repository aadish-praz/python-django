import json

def readuser():
    try:
        with open("user.json","r") as file:
            my_list = json.load(file)
    except FileNotFoundError:
        print("File does not exists")
        return
    except json.JSONDecodeError:
        print("Data does not exists")
        return
    else:
        id = input("\nEnter user id ")
        for item in my_list:
            if item["id"] == id:
                print("Name: ",item["name"])
                print("Age: ",item["age"])
                print("Address: ",item["address"]) 
                
            else:
                print('user doesnot exist')
    