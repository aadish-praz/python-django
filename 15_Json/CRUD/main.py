from create import createuser
from read import readuser
from update import updateuser
from delete import deleteuser

while True:
    choice = input("\nEnter you choice...c/r/u/d ")

    match choice:
        case 'c':
            createuser()
        case 'r':
            readuser()
        case 'u':
            updateuser()
        case 'd':
            deleteuser()
        case _:
            print("\nInvalid choice")

    result = input("\nDo you want to continue y/n ")
    if result == 'n':
        break 
