from connection import connection_db

def updateuser():
    id=int(input('enter the id of user to be updated '))
    column=input('enter the column to be updated(age,Name,Address) ')
    new_value=input(f"enter the new value for {column} ")

    with connection_db() as conn:
        if column=='age':
            
            conn.execute(f''' UPDATE "users" SET {column} ={new_value} WHERE id={id}''') 

        else:
            conn.execute(f''' UPDATE "users" SET {column}={new_value} WHERE id={id}''')
            
    
    with connection_db() as conn:
        if column=='age':
            new_value=int(new_value)
            
        conn.execute(f''' UPDATE "users" SET {column} =? WHERE id=?''',(new_value,id))
            
    
    # with connection_db() as conn:
    #     if column=='age':
            
    #         conn.execute(f''' UPDATE "users" SET "?" =? WHERE id=?''',(column,new_value,id))

    #     else:
    #         conn.execute(f''' UPDATE "users" SET "?" =? WHERE id=?''',(column,new_value,id))
            
    print('\n user updated successfully')


    
    
    
if __name__== "__main__":
    updateuser()