import json

def updateuser():
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
        id = input("\nEnter user id that you want to update ")
        key = input("\nEnter the key that you want to update (e.g. 'name','age','address') ")
        new_value = input(f"\nEnter the new value for {key} ")
        for item in my_list:
            if item["id"] == id:
                item[key] = new_value
                with open("user.json","w") as file:
                    json.dump(my_list,file,indent=4)
                print(f"\nUser with {id} updated!!!")
                break 
        else:
            print(f"\nUser with {id} does not exists")

        
    