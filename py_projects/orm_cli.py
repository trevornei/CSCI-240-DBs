from dotenv import dotenv_values
import sqlalchemy as sa
from sqlalchemy import create_engine

creds = dotenv_values("./.env")

host = creds["host"]
user = creds["user"]
password = creds["password"]
database = creds["database"]

engine = sa.create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
connection = engine.connect()

metadata = sa.MetaData()

staff_table = sa.Table(
    "staff",
    metadata,
    sa.Column("staff_id", sa.Integer, primary_key=True),
    sa.Column("first_name", sa.String(45)),
    sa.Column("last_name", sa.String(45)),
    sa.Column("email", sa.String(50)),
    sa.Column("username", sa.String(16)),
    sa.Column("password", sa.String(40)),
)



print("Assignment: ORM CLI to the Sakila Database.")
print(f"You know have access to the {database}.\n")


print(f"INSTRUCTIONS: CRUD on the staff table.")
print(f"\n    1=CREATE")
print(f"\n    2=READ")
print(f"\n    3=UPDATE")
print(f"\n    4=DELETE")
print(f"\n")
crud_op = input(f"Please select ONE CRUD Operation of your choice. ")

if crud_op == "1": 
    # Gather User Data
    print(f"\n")
    print(f"Let's gather information about the new user that you would like to enter into the database!")
    print(f"\n")
    # fname,lname,email,username,password,store_id
    input_first_name = input(f"|--- FIRST NAME  ---|  ")
    input_last_name = input(f"|--- LAST NAME  ---|  ")
    input_email = input(f"|--- EMAIL ---|  ")
    input_username = input(f"|--- USERNAME ---|  ")
    input_password = input(f"|--- PASSWORD  ---|  ")
    query = sa.insert(staff_table).values(
            {
                "first_name": input_first_name,
                "last_name": input_last_name,
                "email": input_email,
                "username": input_username,
                "password": input_password,
            }
        )
    connection.execute(query)
    connection.commit()
    print(f"\n")
    print(f"You just inserted information into the STAFF table.")
     
if crud_op == "2":
    query = sa.select(
        staff_table.c.first_name,
        staff_table.c.last_name,
        staff_table.c.email,
        staff_table.c.username,
        staff_table.c.password
    )
    result = connection.execute(query)
    for row in result:
        print(f"""
            First_Name: {row.first_name}
            Last_Name: {row.last_name}
            Email: {row.email}
            Username: {row.username}
            password: {row.password}
        """)
    print(f"Result = {result}")

if crud_op == "3": 
    # Gather User Data
    print(f"\n")
    print(f"You have selcected UPDATE.")
    print(f"\n")
    print(f"Please select which user that you would like to update.")
    print(f"\n")
    # fname,lname,email,username,password,store_id
    input_staff_id = input(f"|--- SELECT STAFFER BY STAFF ID ---|  ")
    

    print(f"\n")
    print(f"Enter new staffer details below!")
   

    input_first_name = input(f"|--- NEW FIRST NAME  ---|  ")
    input_last_name = input(f"|--- NEW LAST NAME  ---|  ")
    input_email = input(f"|--- NEW EMAIL ---|  ")
    input_username = input(f"|--- NEW USERNAME ---|  ")
    input_password = input(f"|--- NEW PASSWORD  ---|  ")

    update_query = sa.update(staff_table).where(staff_table.c.staff_id == input_staff_id).values(
            {
                "first_name": input_first_name,
                "last_name": input_last_name,
                "email": input_email,
                "username": input_username,
                "password": input_password,
            }
        )
    connection.execute(update_query)
    connection.commit()
    print(f"\n")
    print(f"You just updated information in the STAFF table.")

if crud_op == "4": 
    # Gather User Data
    print(f"\n")
    print(f"!!!WARNING!!!")
    print(f"\n")
    print(f"!!!You are about to delete a user!!!")
    input_staff_id = input(f"|--- SELECT STAFFER to !delete! BY STAFF ID ---|  ")
    # fname,lname,email,username,password,store_id
    query = sa.delete(staff_table).where(staff_table.c.staff_id == input_staff_id)
    connection.execute(query)
    connection.commit()
    print(f"\n")
    print(f"You have successfully deleted staffer #{input_staff_id}")

print(f"\n")
