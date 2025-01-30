#!/usr/bin/python3

'''
    This Controls The Server, Route And View Of Our App.
'''

from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime, timedelta
import pymysql
import random


app = Flask(__name__)




# For Session Declaration
app.secret_key = 'BAD_SECRET_KEY'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=131040)

# change string to the name of your database; add path if necessary
#db_name = 'sockmarket.db'
username = 'root'
password = "08109214791Chido#"
host = 'localhost'
database = 'kelab'
date = datetime.now()
today = date.strftime("%Y-%m-%d")



@app.route('/', methods =["GET", "POST"])
def index():
    app_name = "Kaleb"
    title = 'Welcome to Kaleb!'
    response = ""
    
    # Access query parameters
    code = request.args.get('code', 'Welcome!') 
    response = request.args.get('response', 'Welcome!') 
    name = request.args.get('name', 'Welcome!') 
    gender = request.args.get('gender', 'Welcome!') 
    arrival_date = request.args.get('arrival_date', 'Welcome!') 
    expected_time = request.args.get('arrival_time', 'Welcome!') 
    
    
    # Connect to MySQL
    conn = pymysql.connect(host='localhost', user='root', password='08109214791Chido#', database='kelab')
    cursor = conn.cursor()
        
    
    try:
        # Execute a query (example: Creating A Users Table)
        if cursor.execute("create table IF NOT EXISTS users(id INT AUTO_INCREMENT, first_name VARCHAR(30) NULL,last_name VARCHAR(30) NULL, email VARCHAR(60) NOT NULL,phone VARCHAR(20) NULL,password VARCHAR(50) NOT NULL,profile_pics VARCHAR(100) NULL,estate_name VARCHAR(50) NULL,apartment_address VARCHAR(100) NULL,flat_number INT NULL,Gender CHAR(20) NULL,country VARCHAR(50) NULL,state CHAR(50) NULL,lga VARCHAR(50) NULL,date_of_birth VARCHAR(30) NULL,occupation VARCHAR(50) NUll,marital_status VARCHAR(50) NULL,religion VARCHAR(50) NULL,role VARCHAR(25) NULL, reg_date CHAR(30) NULL, sign char(20) NULL, primary key(id))"):
            rows = cursor.fetchall()

            # Close the connection
            cursor.close()
            conn.close()

            # Render a template with the data (optional)
            print(f"Database Connected !!!!")
            response = "<div style='background-color: #FFF; box-shadow: 5px 10px #888; color:green; border: 2px #888 solid; border-radius: 20px;'><strong>Kelab:> </strong>*** Database Connected And Users Table Created ***</div><br>"
            
        
        # Execute a query (example: Creating A Visitors Table)
        if cursor.execute("create table IF NOT EXISTS guest(id INT AUTO_INCREMENT, name VARCHAR(80) NULL, gender CHAR(20) NULL, apartment VARCHAR(100) NULL, arrival_date VARCHAR(20) NULL, departure_date CHAR(30) NULL, expected_time_arrival VARCHAR(30) NULL, passcode CHAR(20) NULL, status CHAR(30) NULL, a char(40) NULL, b char(40) NULL, c char(40) NULL, primary key(id))"):
            rows = cursor.fetchall()

            # Close the connection
            cursor.close()
            conn.close()

            # Render a template with the data (optional)
            print(f"Database Connected !!!!")
            response = "<div style='background-color: #FFF; box-shadow: 5px 10px #888; color:green; border: 2px #888 solid; border-radius: 20px;'><strong>Kelab:> </strong>*** Database Connected And Visitors Table Created ***</div><br>"
            

    except pymysql.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return "Error connecting to MySQL"
    
    '''
        This Code Handles The Sign_up Of The Application.
    '''
    if request.method == "POST":
        if request.form.get("owners_role") == "owner":
            
           # getting input with name = first_name etc in HTML form
           email = request.form.get("owners_email") 
           password = request.form.get("owners_password") 
           estate = request.form.get("owners_estate") 
           address = request.form.get("owners_address") 
           flat = request.form.get("owners_flat") 
           role = request.form.get("owners_role")
           reg_date = date.strftime("%d/%m/%y %H:%M:%S")
           #return "Your name is "+email + password + estate + address
           
           if cursor.execute("INSERT INTO users(email, password, estate_name, apartment_address, flat_number, role, reg_date) VALUES('"+email+"', '"+password+"', '"+estate+"', '"+address+"', '"+flat+"', '"+role+"', '"+reg_date+"')"):
               conn.commit()

               # Close the connection
               cursor.close()
               conn.close()

               # Render a template with the data (optional)
               print(f"Database Connected !!!!")
               response = "<div style='background-color: #FFF; box-shadow: 5px 10px #888; color:green; border: 2px #888 solid; border-radius: 20px;'><strong>Kelab:> </strong>*** Congratulations!!! You've Successfully Signed Up. ***</div><br>"
           
        elif request.form.get("form_role") == "login":
            # getting input with name = first_name etc in HTML form
            email = request.form.get("login_email") 
            password = request.form.get("login_password")

            if cursor.execute("SELECT * FROM users WHERE email = '"+email+"' && password='"+password+"' || phone = '"+email+"' && password='"+password+"'"):
                rows = cursor.fetchone()
                
                # Save the form data to the session object
                session['user_id'] = str(rows[0])
                session['first_name'] = str(rows[1])
                session['last_name'] = str(rows[2])
                session['email'] = str(rows[3])
                session['phone'] = str(rows[4])
                session.permanent = True
                                
                response = "<div style='background-color: #FFF; box-shadow: 5px 10px #888; color:green; border: 2px #888 solid; border-radius: 20px;'><strong>Kelab:> </strong>*** Welcome "+str(rows[1])+" "+str(rows[2])+", You Are Successfully Logged In ***</div><br>"
                
                # Close the connection
                cursor.close()
                conn.close()
                
            else:
                response = "<div style='background-color: #FFF; box-shadow: 5px 10px #888; color:green; border: 2px #888 solid; border-radius: 20px;'><strong>Kelab:> </strong>*** No Data Found ***</div><br>"

    return render_template('index.py', title=title, app_name=app_name, response=response, code=code, date=today, name=name, gender=gender, arrival_date=arrival_date, arrival_time=expected_time)
  
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

@app.route('/signup_intro/')
def signup_intro():
    title = 'Sign Up'
    app_name = "Kaleb"
    return render_template('signup_intro.py', title=title, app_name=app_name)

@app.route('/admin_signup/')
def admin_signup():
    title = 'Sign Up'
    app_name = "Kaleb"
    return render_template('admin_signup.py', title=title, app_name=app_name)

@app.route('/owners_signup/')
def owners_signup():
    title = 'Sign Up'
    app_name = "Kaleb"
    return render_template('owners_signup.py', title=title, app_name=app_name)

@app.route('/resident_signup/')
def resident_signup():
    title = 'Sign Up'
    app_name = "Kaleb"
    return render_template('resident_signup.py', title=title, app_name=app_name)

@app.route('/security_signup/')
def security_signup():
    title = 'Sign Up'
    app_name = "Kaleb"
    return render_template('security_signup.py', title=title, app_name=app_name)

@app.route('/security/')
def security():
    title = 'security'
    app_name = "Kaleb"
    return render_template('security.py', title=title, app_name=app_name)

@app.route('/guest/', methods =["GET", "POST"])
def guest():
    title = 'guest'
    app_name = "Kaleb"
    
    # Connect to MySQL
    conn = pymysql.connect(host='localhost', user='root', password='08109214791Chido#', database='kelab')
    cursor = conn.cursor()
    
    if request.method == "POST":
            
       # getting input with name = first_name etc in HTML form
       name = request.form.get("guest_name") 
       gender = request.form.get("guest_gender") 
       arrival_date = request.form.get("arrival_date") 
       address = request.form.get("guest_apartment") 
       atf = request.form.get("arrival_time_from") 
       att = request.form.get("arrival_time_to")
       expected_time = atf+" - "+att
       qr_code = request.form.get("shareQRCode")
       # Generate a random six-digit code
       passcode = random.randint(100000, 999999)
       
       reg_date = date.strftime("%d/%m/%y %H:%M:%S")
       #return "Your name is "+email + password + estate + address
       
       if cursor.execute(""" INSERT INTO guest (name, gender, apartment, arrival_date, expected_time_arrival, passcode, status, c) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """, (name, gender, address, arrival_date, expected_time, passcode, 'pending', qr_code)):
           conn.commit()

           # Close the connection
           cursor.close()
           conn.close()

           # Render a template with the data (optional)
           print(f"Database Connected !!!!")
           response = "<div style='background-color: #FFF; box-shadow: 5px 10px #888; color:green; border: 2px #888 solid; border-radius: 20px;'><strong>Kelab:> </strong>*** Congratulations!!! You've Successfully Booked A Guest For A Visit. ***</div><br>"
       
       else:
           response = "<div style='background-color: #FFF; box-shadow: 5px 10px #888; color:red; border: 2px #888 solid; border-radius: 20px;'><strong>Kelab:> </strong>***  Technical Database Error Enquired ***</div><br>"
    
    return redirect(url_for('index', _anchor='visitors_code', name=name, gender=gender, arrival_date=arrival_date, arrival_time=expected_time, response=response, code=passcode))


@app.route('/logout/')
def logout():
    title = 'logout'
    app_name = "Kaleb"
    
    # Clear the email stored in the session object
    session.pop('user_id', default=None)
    session.pop('first_name', default=None)
    session.pop('last_name', default=None)
    session.pop('email', default=None)
    session.pop('phone', default=None)
    
    response = "<div style='background-color: #FFF; box-shadow: 5px 10px #888; color:red; border: 2px #888 solid; border-radius: 20px;'><strong>Kelab:> </strong>***  You Just Logged Out, Come Back Soon !!! ***</div><br>"
    
    return render_template('index.py', title=title, app_name=app_name, response=response)

if __name__ == '__main__':
    app.run(debug=True)