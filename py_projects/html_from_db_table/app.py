from flask import Flask, render_template, request, logging
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

@app.route("/", methods=["POST", "GET"])
def users_table():
    # SQL Statement, create cursor, fetch the data from the request, close the connection to the db.
    request_users = f"SELECT * FROM users;"
    request_cursor = cnx.cursor()
    request_cursor.execute(request_users)
    # In index.html use jinja2 to create a for loop for the data that is fetched from users variable...
    users = request_cursor.fetchall()
    request_cursor.close()
    
    # Render the html...
    return render_template("index.html", users=users)

