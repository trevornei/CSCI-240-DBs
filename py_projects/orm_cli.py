import mysql.connector
from dotenv import dotenv_values
from mysql.connector import (connection)

creds = dotenv_values("./.env")

host = creds["host"]
user = creds["user"]
password = creds["password"]
database = creds["database"]

cnx = connection.MySQLConnection(host=host, user=user, password=password, database=database)
curse = cnx.cursor()

print("Assignment: ORM CLI to the Sakila Database.")
print(f"You know have access to the {database}.\n")


print(f"INSTRUCTIONS: CRUD on the staff table.")
print(f"\n    1=CREATE")
print(f"\n    2=READ")
print(f"\n    3=UPDATE")
print(f"\n    4=DELETE")
print(f"\n")
crud_op = input(f"Please select ONE CRUD Operation of your choice. ")
print(f"\n")

# CRUD Fn()'s
def c():
    print("To create a table you must give us a name.")
    print(f"Table created..")


def r(): 
    print("Read")

def u():
    print("Update")

def d(): 
    print("Delete")

cnx.close()
