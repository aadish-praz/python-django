from connection import connection_db

with connection_db() as conn:
    conn.execute(
        
        f'''
        
        CREATE TABLE IF NOT EXISTS users(
            
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            address TEXT
        )
        '''
        
    )