import json

def deleteuser():
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
        id = input("\nEnter user id that you want to delete")
        for item in my_list:
            if item["id"] == id:
                my_list.remove(item)
                print(f"\nUser with {id} deleted!!!")
                with open("user.json","w") as file:
                    json.dump(my_list,file,indent=4)
                break 
        else:
            print(f"\nUser with {id} does not exists")

        
    