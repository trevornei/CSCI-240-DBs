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
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("first_name", sa.String(45)),
    sa.Column("last_name", sa.String(45)),
    sa.Column("email", sa.String(50)),
    sa.Column("username", sa.String(16)),
    sa.Column("password", sa.String(40))
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

