from aifc import Error

import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print(db_name)
        print(" ПОДКЛЮЧЕНИЕ УСПЕШНО! PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


# вызываем функцию подключения с текущими параметрами БД
connection = create_connection(
    "postgres", "elijahswanson", "abc123", "127.0.0.1", "5432"
)


def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_database_query = "CREATE DATABASE my_db_pets"
create_database(connection, create_database_query)

connection = create_connection(
    "my_db_pets", "elijahswanson", "abc123", "127.0.0.1", "5432"
)


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(connection)
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# параметр для добавления новой таблицы в созданную БД
create_pets_table = """
create table PETSALE (
	ID INTEGER PRIMARY KEY NOT NULL,
	ANIMAL VARCHAR(20),
	QUANTITY INTEGER,
	SALEPRICE DECIMAL(6,2),
	SALEDATE DATE
	);
"""
# добавляем в БД таблицу с инфо о животных
execute_query(connection, create_pets_table)

# добавляем животных
pets = [
    (1, 'Cat', 9, 450.09, '2018-05-29'),
    (2, 'Dog', 3, 666.66, '2018-06-01'),
    (3, 'Dog', 1, 100.00, '2018-06-04'),
    (4, 'Parrot', 2, 50.00, '2018-06-04'),
    (5, 'Dog', 1, 75.75, '2018-06-10'),
    (6, 'Hamster', 6, 60.60, '2018-06-11'),
    (7, 'Cat', 1, 44.44, '2018-06-11'),
    (8, 'Goldfish', 24, 48.48, '2018-06-14'),
    (9, 'Dog', 2, 222.22, '2018-06-15')

]

pets_records = ", ".join(["%s"] * len(pets))

insert_query = (
    f"INSERT INTO PETSALE (ID, ANIMAL, QUANTITY, SALEPRICE, SALEDATE ) VALUES {pets_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, pets)


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


select_pets = "SELECT * FROM PETSALE"
pets = execute_read_query(connection, select_pets)
# выводим данные на экран
for pet in pets:
    print(pet)
