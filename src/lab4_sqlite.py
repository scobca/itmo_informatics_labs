from sqlite3 import Error
from sqlite3 import connect
import migrations.queries as queries

def create_connection(path):
    try:
        connection = connect(path)
        print("Connection successful")
    except Error as e:
        print(e)

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed")
    except Error as e:
        print(e)


connection = create_connection('db/lab4.sqlite')

execute_query(connection, queries.create_authors_table)
execute_query(connection, queries.create_books_table)
execute_query(connection, queries.create_readers_table)
execute_query(connection, queries.create_orders_table)

# Добавляем авторов
# execute_query(connection, queries.create_authors)

