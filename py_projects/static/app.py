from flask import Flask
from mysql.connector import (connection)
from dotenv import dotenv_values
app = Flask(__name__)

import mysql.connector
creds = dotenv_values("./.env")

host = creds["host"]
user = creds["user"]
password = creds["password"]
database = creds["database"]

cnx = mysql.connector.connect(host=host, user=user , password=password, database=database)

# Created a decorator fn for the default route. 
@app.route("/")
def table_one():
    test_webserver = "This is a flask application"

    return test_webserver


