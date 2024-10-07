from connection import connection_db

def createuser():
    name=input('enter the name of the person ')
    age=int(input('Enter the age of the person '))
    address=input('enter the address of the person' )


    # with connection_db() as conn:
    #     conn.execute(
            
    #         f'''
            
    #         INSERT INTO 'users' ('name','age','address') VALUES ('{name}',{age},'{address}')
            
            
    #         '''
    #         ,(name,age,address)
    #     )
    
    
    
    with connection_db() as conn:
        conn.execute(
            
            f'''
            
            #comment INSERT INTO 'users' ('name','age','address') VALUES ('{name}',{age},'{address}')
            INSERT INTO 'users' ('name','age','address') VALUES (?,?,?)
            
            '''
            ,(name,age,address)
        )
    print('\n user created successfully')
    
if __name__=="__main__":
    createuser()