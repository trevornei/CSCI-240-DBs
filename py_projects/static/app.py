from flask import Flask, render_template
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
    cursor = cnx.cursor()
    query = f"SELECT * FROM users;"
    # Now I execute the query
    cursor.execute(query)
    users = cursor.fetchall()
    return render_template("./index.html", users=users)


