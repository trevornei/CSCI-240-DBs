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
print(f"The value of Host: {host}\n The value of User: {user}\n The value of PW: {password}\n The value DB: {database}")

# Connects to the database with IPC path(Unix Interprocess communication)
# I found out that I have to have a variable for the unix_socket if I'm using loopback local for the host address. 
#   ---> this is because mysqlconnect library defaults to using tcp instead of ICP.
cnx = connection.MySQLConnection(host=host, user=user, password=password, database=database, unix_socket=unix_socket)


# shutdown chnl. ----X
cnx.close()
