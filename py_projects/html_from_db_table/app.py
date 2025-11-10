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
    
    if request.method == "POST":
        # Get form data from the user.
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        user_name = request.form.get('uname')  # Note: no username field in form currently
        email = request.form.get('email')
        
        form_cursor = cnx.cursor()
        update_users_table = """
            INSERT INTO users(first_name, last_name, user_name, email)
            VALUES(%s, %s, %s, %s)
        """
        # Param1: Insert statement
        # Param2: values that are passed into the database
        form_cursor.execute(update_users_table, (first_name, last_name, user_name, email))
        cnx.commit()
        form_cursor.close()
    # Render the html...
    return render_template("index.html", users=users)

