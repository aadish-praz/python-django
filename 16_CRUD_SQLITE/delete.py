from connection import connection_db

def deleteuser():
    id=int(input('enter the id of user '))

    # with connection_db() as conn:
    #     data=conn.execute(
    #         f'''
            
    #         DELETE  FROM users where id={id}
    #         '''
            
    #     )
        
    with connection_db() as conn:
        data=conn.execute(
            f'''
            
            DELETE  FROM users where id=?
            
            ''',(id,)
            
        )
        
    
    print(f'User with user {id} deleted successfully')
    
if __name__== "__main__":
    deleteuser()