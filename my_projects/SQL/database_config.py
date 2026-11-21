import psycopg as pg

YOUR_PASSWORD = "1111"

def get_connection():
    return pg.connect( 
        dbname="postgres",
        user="postgres",
        password=YOUR_PASSWORD,
        host="localhost"
    )
