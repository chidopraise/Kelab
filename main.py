#!/usr/bin/python3

'''
    This Controls The Server, Route And View Of Our App.
'''

from flask import Flask, render_template, request
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.sql import text
import pymysql


# this variable, db, will be used for all SQLAlchemy commands
#db = SQLAlchemy()

app = Flask(__name__)


# change string to the name of your database; add path if necessary
#db_name = 'sockmarket.db'
username = 'root'
password = "08109214791Chido#"
host = 'localhost'
database = 'kelab'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + username + ':' + password + '@' + host + database

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize the app with Flask-SQLAlchemy
#db.init_app(app)



@app.route('/', methods =["GET", "POST"])
def index():
    app_name = "Kaleb"
    title = 'Welcome to Kaleb!'
    try:
        # Connect to MySQL
        conn = pymysql.connect(host='localhost', user='root', password='08109214791Chido#', database='kelab')
        cursor = conn.cursor()

        # Execute a query (example: fetch all rows from a table)
        cursor.execute("SHOW TABLES")
        row = cursor.fetchall()
        
        #cursor.execute("create table IF NOT EXISTS users(id INT AUTO_INCREMENT, first_name VARCHAR(30) NOT NULL,last_name VARCHAR(30) NOT NULL,middle_name VARCHAR(30) NULL, user_name VARCHAR(20) NOT NULL,email VARCHAR(60) NOT NULL,phone VARCHAR(20) NULL,password VARCHAR(50) NOT NULL,profile_pics VARCHAR(100) NULL,address VARCHAR(100) NULL,sex CHAR(20) NULL,country VARCHAR(50) NULL,state CHAR(50) NULL,date_of_birth VARCHAR(30) NULL,postal_code INT NULL,lga VARCHAR(50) NULL,profession VARCHAR(50) NUll,marital_status VARCHAR(50) NULL,religion VARCHAR(50) NULL,nk_name VARCHAR(50) NULL,nk_phone VARCHAR(20) NULL, presence INT NULL, date CHAR(30) NULL, sign char(20) NULL, primary key(id))")
        #rows = cursor.fetchall()

        # Close the connection
        cursor.close()
        conn.close()

        # Render a template with the data (optional)
        print(f"Database Connected")
        return render_template('index.py', data=row) 

    except pymysql.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return "Error connecting to MySQL"
    
    '''
        This Code Handles The Sign_up Of The Application.
    '''
    if request.method == "POST":
       # getting input with name = first_name etc in HTML form
       email = request.form.get("email") 
       password = request.form.get("password") 
       estate = request.form.get("estate") 
       address = request.form.get("address") 
       return "Your name is "+email + password + estate + address
    return render_template('index.py', title=title, app_name=app_name)
    
@app.route('/home/')
def home():
    title = 'home'
    app_name = "Kaleb"
    return render_template('home.py', title=title, app_name=app_name)

@app.route('/visitors/')
def visitors():
    title = 'Visitors'
    app_name = "Kaleb"
    return render_template('visitors.py', title=title, app_name=app_name)
    
@app.route('/payments/')
def payments():
    title = 'Payments'
    app_name = "Kaleb"
    return render_template('payments.py', title=title, app_name=app_name)

@app.route('/residents/')
def residents():
    title = 'Residents'
    app_name = "Kaleb"
    return render_template('residents.py', title=title, app_name=app_name)
    
@app.route('/visitors_code/')
def visitors_code():
    title = "Visitors Code"
    app_name = "Kaleb"
    return render_template("visitors_code.py", title=title, app_name=app_name)

@app.route('/owner/')
def owner():
    title = 'Owner'
    app_name = "Kaleb"
    return render_template('owner.py', title=title, app_name=app_name)

@app.route('/monthly_dues/')
def monthly_dues():
    title = 'Monthly_Dues'
    app_name = "Kaleb"
    return render_template('monthly_dues.py', title=title, app_name=app_name)

@app.route('/profile/')
def profile():
    title = 'Profile'
    app_name = "Kaleb"
    return render_template('profile.py', title=title, app_name=app_name)

@app.route('/reg_residents/')
def reg_residents():
    title = 'Reg Residents'
    app_name = "Kaleb"
    return render_template('reg_residents.py', title=title, app_name=app_name)

@app.route('/signin/')
def signin():
    title = 'Sign In'
    app_name = "Kaleb"
    return render_template('signin.py', title=title, app_name=app_name)

@app.route('/signup/')
def signup():
    title = 'Sign Up'
    app_name = "Kaleb"
    return render_template('signup.py', title=title, app_name=app_name)

@app.route('/security/')
def security():
    title = 'security'
    app_name = "Kaleb"
    return render_template('security.py', title=title, app_name=app_name)

if __name__ == '__main__':
    app.run(debug=True)