import mysql.connector
from dotenv import dotenv_values
from mysql.connector import (connection)

creds = dotenv_values(".env")
print(creds)

# Create vars: host, user, password, database

host = creds["host"]
user = creds["user"]
password = creds["password"]
database = creds["database"]
unix_socket = creds["unix_socket"]

# print(f"The value of Host: {host}\n The value of User: {user}\n The value of PW: {password}\n The value DB: {database}")

# Connects to the database with IPC path(Unix Interprocess communication)
# I found out that I have to have a variable for the unix_socket if I'm using loopback local for the host address. 
#   ---> this is because mysqlconnect library defaults to using tcp instead of ICP.
cnx = connection.MySQLConnection(host=host, user=user, password=password, database=database, unix_socket=unix_socket)

print("Welcome and wake up Neo.")
print(f"You know have access to the {database}.\n You know who the birds work for.")

name = input("What is your name Neo?")
print(f"Neo, it's good to meet you {name}..?")
print("Anyways...")
print(f"\n Here are your options:")
print(f"\n 1=CREATE")
print(f"\n 2=READ")
print(f"\n 3=UPDATE")
print(f"\n 4=DELETE")

# Gather the input
crud_op = input(f"Please select the CRUD Operation of your choice. ")

# shutdown chnl. ----X
cnx.close()
