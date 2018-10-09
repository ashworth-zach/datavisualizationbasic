from flask import Flask, redirect, render_template, request, flash
import pymysql.cursors
import datetime

# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
mysql = connectToMySQL("leads")

app = Flask(__name__)
@app.route('/')
def index():
    all_leads = mysql.query_db("SELECT * FROM employees")
    print(all_leads)
    return render_template('index.html', leads = all_leads)
# @app.route('/process', methods=['POST'])
# def process():
#     mysql = connectToMySQL("leads")
#     query = "INSERT INTO leads (first_name, last_name, occupation, created_at, updated_at) VALUES (%(firstname)s, %(lastname)s, %(leads)s, NOW(), NOW());"
#     firstname= request.form['firstname']
#     lastname=  request.form['lastname']
#     leads= request.form['leads']
#     data={
#         'firstname':firstname,
#         'lastname':lastname,
#         'leads':leads
#     }
#     new_friend_id = mysql.query_db(query, data)
#     return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)
