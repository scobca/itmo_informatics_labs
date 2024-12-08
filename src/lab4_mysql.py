import mysql.connector
from mysql.connector import Error
import migrations.mysql_queries as queries


def create_connection_without_db(host, user, password):
    connect = None
    try:
        connect = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
        )
        print("Connection successful")
    except Error as e:
        print(e)

    return connect


def create_db(connect, query):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(e)


def create_connection(host, user, password, database):
    connect = None
    try:
        connect = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database,
        )
        print("Connection successful")
    except Error as e:
        print(e)

    return connect


connection = create_connection_without_db('localhost', 'root', 'Uw2xwUxMOmo')
create_db(connection, 'CREATE DATABASE IF NOT EXISTS lab4')

connection = create_connection('localhost', 'root', 'Uw2xwUxMOmo', 'lab4')


def execute_query(connect, query):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        connect.commit()
        print("Query executed successfully")
    except Error as e:
        print(e)


def execute_read_query(connect, query):
    cursor = connect.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



execute_query(connection, queries.create_authors_table)
execute_query(connection, queries.create_books_table)
execute_query(connection, queries.create_readers_table)
execute_query(connection, queries.create_orders_table)

# Добавляем авторов, книги, читателей, заказы
# execute_query(connection, queries.create_authors)
# execute_query(connection, queries.create_books)
# execute_query(connection, queries.create_readers)
# execute_query(connection, queries.create_orders)

# Выбираем все записи из таблицы books
execute_read_query(connection, "SELECT * FROM books")

print(" ")

# Получаем информацию о книгах и их авторах, используя join
res = execute_read_query(connection, queries.join_query_get_books)
for r in res:
    print(r)

print(" ")

# Получаем информацию о кол-ве читателей, у которых автор стоит как "Любимый автор". Группируем по полю favourite_author
res = execute_read_query(connection, queries.where_query_get_readers)
for r in res:
    print(r)

print(" ")


# Вложенные запросы
# 1 - получаем имена и дату регистрации пользователей, у которых любимый автор - Достоевский
# 2 - получаем заказы (имя, книга), в которых автор книги родился после 1850 года
res = execute_read_query(connection, queries.nested_query_1)
for r in res:
    print(r)

print(" ")

res = execute_read_query(connection, queries.nested_query_2)
for r in res:
    print(r)

print(" ")


# Union запросы
# 1 - выводим одновременно имена пользователей и имена авторов книг
# 2 - выводим одновременно имена пользователей и названия книг

res = execute_read_query(connection, queries.union_query_1)
for r in res:
    print(r)

print(" ")

res = execute_read_query(connection, queries.union_query_2)
for r in res:
    print(r)

print(" ")


# Distinct запросы: выведем имена пользователей без повторения.

# Создадим еще одного Иванова Ивана Ивановича
execute_query(connection, 'INSERT INTO readers (name, registration_date, favourite_author) VALUES ("Иванов Иван Иванович", "2023-07-22", 4)')

# В результате запроса получаем только 1 Иванова Ивана Ивановича
res = execute_read_query(connection, queries.distinct_query)
for r in res:
    print(r)

print(" ")


# Update queries
# 1
print(execute_read_query(connection, "Select readers.name From readers Where id = 1"))
execute_read_query(connection, queries.update_query_1)
print(execute_read_query(connection, "Select readers.name From readers Where id = 1"))

print(" ")

# 2
print(execute_read_query(connection, "Select authors.author_name From authors Where id = 2"))
execute_read_query(connection, queries.update_query_2)
print(execute_read_query(connection, "Select authors.author_name From authors Where id = 2"))

print(" ")


# Delete queries

execute_read_query(connection, queries.setting_query)


print(execute_read_query(connection, "Select * From readers"))
execute_read_query(connection, queries.delete_query_1)
print(execute_read_query(connection, "Select * From readers"))

print(" ")

print(execute_read_query(connection, "Select * From authors"))
execute_read_query(connection, queries.delete_query_2)
print(execute_read_query(connection, "Select * From authors"))

print(" ")

print(execute_read_query(connection, "Select * From books"))
execute_read_query(connection, queries.delete_query_3)
print(execute_read_query(connection, "Select * From books"))

print(" ")

print(execute_read_query(connection, "Select * From orders"))
execute_read_query(connection, queries.delete_query_4)
print(execute_read_query(connection, "Select * From orders"))

print(" ")

# Delete all
print(execute_read_query(connection, "Select * From readers"))
execute_read_query(connection, queries.delete_all_readers_query)
print(execute_read_query(connection, "Select * From readers"))
