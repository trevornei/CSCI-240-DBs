from flask import Flask, render_template, request, redirect, url_for, logging
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
    request_cursor = cnx.cursor(buffered=True)
    request_cursor.execute(request_users)
    # In index.html use jinja2 to create a for loop for the data that is fetched from users variable...
    users = request_cursor.fetchall()
    request_cursor.close()
    
    if request.method == "POST":
        # Create a variable to store the value of the user selected radio button.
        selected_radio_button = request.form.get('crud')
        # Get form data from the user.
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        user_name = request.form.get('uname') 
        email = request.form.get('email')
        
        form_cursor = cnx.cursor(buffered=True)

        if selected_radio_button == "create":
            create_user = """
            INSERT INTO users(first_name, last_name, user_name, email)
            VALUES(%s, %s, %s, %s)
            """
            form_cursor.execute(create_user, (first_name, last_name, user_name, email))
        
        elif selected_radio_button == "read":
            # This redirect allow the user to "read" by refreshing the page for the latest results which runs the select
            # all query against the db.
            return redirect(url_for("users_table"))

        elif selected_radio_button == "update":
            pass

        elif selected_radio_button == "delete":
            pass

        cnx.commit()
        form_cursor.close()
    # Render the html...
    return render_template("index.html", users=users)

