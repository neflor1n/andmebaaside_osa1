import json
from sqlite3 import *
from sqlite3 import Error
from os import *
import time
from tkinter import *
import tkinter as tk

def connect_to_db(path: str):
    connection = None
    try:
        connection =connect(path)
        print("Connected was successful")
    except Error as e:
        print(f'Tekkis viga: {e}')
    return connection

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel created")
    except Error as e:
        print(f'Tekkis viga: {e}')

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except Error as e:
        print(f'Tekkis viga: {e}')

def execute_insert_query(connection, data):


    query = "INSERT INTO users(Name, Last_name, Age, Car, Pets) values (?, ?, ?, ?, ?)"
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()


def execute_insert_query_cars(connection, data):
    query = "INSERT INTO cars(carMark, carModel, carNum, carOwner) values (?, ?, ?, ?)"
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()

def drop_table(connection, table):
    try:
        cursor = connection.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
        connection.commit()
    except Error as e:
        print(f'Tekkis viga: {e}')


def find_name_by_letter(connection, letter):
    try:

        cursor = connection.cursor()
        param = f"{letter}%"
        query = f"SELECT * FROM users WHERE Name LIKE {param}"
        cursor.execute(query, (param,))
        results = cursor.fetchall()


        return results

    except Error as e:
        print(f'Tekkis viga: {e}')
        return []





create_users_table = """
CREATE TABLE IF NOT EXISTS users(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL,
Last_name TEXT NOT NULL,
Age INTEGER NOT NULL,
Car BOOLEAN NOT NULL,
Pets BOOLEAN NOT NULL)
"""

create_cars_table = """
CREATE TABLE IF NOT EXISTS cars(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
carMark TEXT NOT NULL,
carModel TEXT NOT NULL,
carNum TEXT NOT NULL,
carOwner INTEGER NOT NULL,
foreign key (carOwner) references users(Id))
"""



insert_users = """
INSERT INTO users (Name, Last_name, Age, Car, Pets)
VALUES ("Bogdan", "Sergachev", 16, False, True),
("Gleb", "Sotsjov", 16, False, True),
("Kirill", "Sats", 16, False, True),
("Vsevolod", "Tsarev", 16, False, True),
("Martin", "Sild", 16, False, True)
"""

insert_cars = """
INSERT INTO cars (carMark, carModel, carNum, carOwner)
VALUES ("BMW", "M3", "123 ABC", 1),
("Audi", "r6", "414 CMD", 2),
("BMW", "M5 F90", "581 ASJ", 3),
("BMW", "M4 Competition", "175 JSN", 4),
("Audi", "r8", "758 ASH", 5)
"""

drop_table_user = """
DROP TABLE IF EXISTS users """
drop_table_car = """
DROP TABLE IF EXISTS cars """

select_users = "SELECT * FROM users"
select_cars = "SELECT * FROM cars"

filename = path.abspath(__file__)
dbdir = filename.rsplit('andmebaaside.py')
current_dir = getcwd()
dbpath = path.join(current_dir, 'data.db')
conn = connect_to_db(dbpath)

# ----------------------- DROP TABLES -----------------------

execute_query(conn, drop_table_user)
execute_query(conn, drop_table_car)

# ----------------------- CREATE TABLES -----------------------

execute_query(conn, create_users_table)
execute_query(conn, create_cars_table)

# ----------------------- INSERT INTO TABLES -----------------------

execute_query(conn, insert_users)
execute_query(conn, insert_cars)
# insert_user = input("Name: "), input("Last name: "), int(input("age:")), int(input("Car (1(TRUE) OR 0(FALSE)):")), int(input("Pets (1(TRUE) OR 0(FALSE)): "))
# execute_insert_query(conn, insert_user)
#
# insert_car = input("CarMake: "), input("CarModel: "), input("CarNum: "), int(input("CarOwner (ID FROM TABLE 'USERS'!!!): "))
# execute_insert_query_cars(conn, insert_car)

# ----------------------- READ TABLES -----------------------

users = execute_read_query(conn, select_users)
cars = execute_read_query(conn, select_cars)


# ----------------------- OUTPUTTING TABLES -----------------------
# print("Kautajate tabel #users#: ")
# for user in users:
#     print(user)

# print("Kautajate tabel #cars#: ")
# print(cars)





while True:


    print('\n----------- MENU ------------')
    valikNum = int(input('1 - View users table \n2 - View cars table \n3 - insert into users table \n4 - insert into cars table \n5 - delete table\n6 - Find name with letter \n"----------------------------"\nEnter a number: '))
    if valikNum == 1:
        print("Kautajate tabel #users#: ")
        select_users = """SELECT * FROM USERS"""
        for user in users:
            print(user)
    elif valikNum == 2:
        print("Kautajate tabel #cars#: ")
        select_cars = """SELECT * FROM CARS"""
        print(cars)
    elif valikNum == 3:
        insert_user = input("Name: "), input("Last name: "), int(input("age:")), int(
            input("Car 1 = TRUE OR 0 = FALSE:")), int(input("Pets 1 = TRUE OR 0 = FALSE: "))
        execute_insert_query(conn, insert_user)
        select_users = """SELECT * FROM USERS"""
        users = execute_read_query(conn, select_users)
        for user in users:
            print(user)

    elif valikNum == 4:
        insert_cars = input("CarMake: "), input("CarModel: "), input("CarNum: "), int(
            input("CarOwner (ID FROM TABLE 'USERS'!!!): "))
        execute_insert_query_cars(conn, insert_cars)
        select_cars = """SELECT * FROM CARS"""
        cars = execute_read_query(conn, select_cars)
        print(cars)
    elif valikNum == 5:
        drop_table = input("Dropping table? (Yes/No): ").capitalize()
        if drop_table == "Yes":
            drop_tablee = input("Which table would you like to drop?: ").lower()
            drop_table(conn, drop_tablee)
        elif drop_table == "No":
           break
    elif valikNum == 6:
        letter = input("First Letter: ")
        find_name_by_letter(conn, letter)




#execute_query(conn, drop_table_user)






