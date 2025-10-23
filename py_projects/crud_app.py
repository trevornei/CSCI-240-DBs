import mysql.connector
from dotenv import dotenv_values
from mysql.connector import (connection)

creds = dotenv_values("../.env")
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
curse = cnx.cursor()

print("Welcome and wake up Neo.")
print(f"You know have access to the {database}.\n You know who the birds work for.")

name = input("What is your name Neo?")
print(f"Neo, it's good to meet you {name}..?")
print("Anyways...")
print(f"\n Here are your options:")
print(f"\n Modulate Tables")
print(f"\n 1=CREATE")
print(f"\n 2=READ")
print(f"\n 3=UPDATE")
print(f"\n 4=DELETE")
print(f"\n")
print(f"\n Paper = if you wish to enter the Print Que")
print(f"\n")
print(f"\n")
# Gather the input
crud_op = input(f"Please select the CRUD Operation of your choice. ")
print(f"\n")
print(f"\n")
# CRUD Fn()'s
def c():
    print("To create a table you must give us a name.")
    cTable = input(f"Write Name Here: ")
    new_table = f"""
        CREATE TABLE IF NOT EXISTS {cTable} (
            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            name VARCHAR(100) NOT NULL,
            PRIMARY KEY (id)
        )
    """
    curse.execute(new_table)
    cnx.commit()
    print(f"Table created..")


def r(): 
    print("Read")
    rTable = input(f"What Table do you want to read? Shouldn't you be waking up Neo?").strip()
    read_table = f"SELECT * FROM {rTable}"
    curse.execute(read_table)
    rows = curse.fetchall()
    print(f"This is a row {rows}")

def u():
    print("Update")
    tbl = input("Table name: ").strip()
    set_col = input("Column/Attribute to update: ").strip()
    where_col = input("WHERE column (This is yurrr ID Value): ").strip()
    new_val = input("New value: ")
    where_val = input("Value to match in WHERE: ")

    # Feeeeeeed the SQL statement with the params <3 
    sql = f"UPDATE `{tbl}` SET `{set_col}` = %s WHERE `{where_col}` = %s"
    # Has to pass in statement to execute and params >:-)
    curse.execute(sql, (new_val, where_val))
    cnx.commit()

    print(f"Updated {curse.rowcount} row(s).")


def d(): 
    print("Delete")
    dTable = input(f"Please suggest which T a b l e that you'd like to select.")
    delete_table = f"DROP TABLE {dTable}"
    curse.execute(delete_table)
    cnx.commit()
    print("Good job Neo – you dropped the Matrix.")

# This function runs a sql join statment...
def users_feeds():
    print("You can find how many times a given user appears in any given feed. \n")
    collect_user = input("Which user would you like to select?")
    collect_feed = input("Which feed would you like to select?")
    join_tables = f"""
      SELECT user_id
      FROM users 
      INNER JOIN feeds 
      ON users.user_id = feeds.user_id;
    """ 
    curse.execute(join_tables)
    cnx.commit()
    print(f"Done.")


def add_user_feed():
    print(f"You are about add a user to a feed.")

def remove_user_feed():
    print(f"You are about to remvoe a user to a feed. Proceed with caution.")
"""

Assignment Part Two: 

"""

def var_rate_mortgage():
    print("Good job Neo – you dropped the Matrix.")
    print(f"Neo, don't read The Big Short.")
    print(f"\n Anyways...")
    print(f"""
              Your Options are:
                Press "one" for print users;
                Press "two" for print feeds;
                Press "three" for printing users in a feed;
                Press "four" for printing feeds that a user appears in;
                Press "five" for adding a user;
                Press "six" for removing a user;
                Press "seven" or "Quit" for QUITTING THE PROGRAM!;

          """)
    originate_sell = input(f"\n Please select your choice here.")
    
    if originate_sell == "one" or originate_sell == "two":
        r()
    
    elif originate_sell == "three":
        print(f"Welcome - you will be printing how many times a user appears in a given feed.")
        users_feeds()        

    elif originate_sell == "four": 
        print(f"Welcome to step four")

    elif originate_sell == "five": 
        print(f"Welcome to step five. Add a user to a feed.")
        add_user_feed()

    elif originate_sell == "six": 
        print(f"Welcome to step six. REMOVE a user of a feed.")
        remove_user_feed() 

    elif originate_sell == "Quit" or originate_sell == "quit" or originate_sell == "7": 
        print(f"closing session")
        cnx.close()
        print(f"S E S S I O N -----X ClOSED --X")

# Condition flooooow determines which CRUD fn to call() <:]
if crud_op == "1":
    c()

elif crud_op == "2":
    r()

elif crud_op == "3":
    u()

elif crud_op == "4":
    d()

elif crud_op == "Paper" or crud_op == "paper":
    var_rate_mortgage()

elif crud_op == "Quit" or crud_op == "quit":
    print(f"closing session")
    cnx.close()
    print(f"S E S S I O N -----X ClOSED --X")
# shutdown chnl. ----X
cnx.close()
