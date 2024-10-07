from connection import connection_db

def readuser():
    id=int(input('enter the id of user '))


    # with connection_db() as conn:
    #     data=conn.execute(
    #         f'''
            
            
            
    #         SELECT * FROM "users" WHERE "id"={id}
    #         '''
            
    #     ).fetchone()
        
        
    with connection_db() as conn:
        data=conn.execute(
            f'''
            
            SELECT * FROM "users" WHERE "id"=?
            ''',(id,)
            
        ).fetchone()
        
    print(data)
    print('\n Name :',data[1])
    print(' Age :',data[2])
    print('Address :',data[3])
    
    
    
if __name__== "__main__":
    readuser()