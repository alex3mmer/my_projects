import database_config 
from contextlib import closing

def initialize_database():
    with closing(database_config.get_connection()) as connection:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS my_table (
                        id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
                        name VARCHAR(100) NOT NULL, 
                        age INT NOT NULL
                    )
                """)

def add_user(name, age):
    with closing(database_config.get_connection()) as connection:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO my_table (name, age) VALUES (%s, %s)",
                    (name, age)
                )


def show_users():
    with closing(database_config.get_connection()) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM my_table")

            return cursor.fetchall()

"""with closing(database_config.get_connection()) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM my_table")
        rows = cursor.fetchall()

        for row in rows:
            print(row)"""