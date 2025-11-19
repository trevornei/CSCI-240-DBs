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
# Created a decorator fn for the default route. 
@app.route("/", methods=["POST", "GET"])
def get_pigeon_food():
    print(f"{request.method =}")
    if request.method == "POST" or request.method == "GET":
        add_cursor = cnx.cursor()

        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        email = request.form.get('email')
        print(f"{first_name}, {last_name}, {email}")
        # I created two variables that separate the insert statement and the values statement.
        mysql_insert = f"INSERT INTO users(first_name, last_name, email) VALUES (%s, %s, %s)"
        form_values = (first_name, last_name, email)
        add_cursor.execute(mysql_insert, form_values)
        cnx.commit()
    return render_template("index.html")

@app.route("/funky-table", methods=["POST", "GET"])
def generate_table():
    cursor = cnx.cursor()
    query = f"SELECT * FROM users;"
    # Now I execute the query
    cursor.execute(query)
    users = cursor.fetchall()
    return render_template("./funky-table.html", users=users)



