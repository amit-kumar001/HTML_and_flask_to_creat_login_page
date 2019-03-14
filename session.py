# __version__ = '0.1.0'
from flask import Flask,request,url_for, redirect, render_template,logging,session,request,flash
import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", password="Server@123", database="joins")
print("connection successful")
cursor = db.cursor()



# TOPIC_DICT = __version__
app = Flask(__name__)
#Constructor with argument



@app.route('/index', methods = ['GET','POST'])
def index():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      cursor.execute("SELECT count(1) FROM register WHERE username = %s;", [username])  # CHECKS IF USERNAME EXSIST
      if cursor.fetchone()[0]:
         cursor.execute("SELECT count(1) FROM register WHERE password = %s;", [password])# FETCH THE HASHED PASSWORD
         if cursor.fetchone()[0]:   # if request.form['password'] == 'password' and request.form['username'] == 'admin':
38
   #    session['logged_in'] = True
39
   # else:
40
   #    flash('wrong password!')
41
   # return "try again"
           return "thank you"
  \
         else:
          return "Check password"
      else:
         return"check username and password"

   return render_template('sigin.html')









@app.route('/login', methods = ['POST'])
#Route() function in which we can  represent URL ,
#also, define methods  that used to send data to a server to create/update a resource
def login():
   if request.method == 'POST':# request method to use 'POST'
      name = request.form['name']# syntax to use get() method &&&&
      l_name = request.form['l_name']
      username = request.form['username']
      password = request.form['password']
      address = request.form['address']
      phone = request.form['phone']
      email = request.form['email']
      pincode=request.form['pincode']


      db = mysql.connector.connect(host="localhost", user="root", password="Server@123", database="joins")
      print("connection successful")
      cursor = db.cursor()

      sql = "INSERT INTO register(name, l_name, username, password, address, phone, email, pincode) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"

      val = ([name, l_name, username, password, address, phone, email, pincode])
      cursor.execute(sql, val)
      db.commit()
      db.close()

      return redirect(url_for('index'))

   return render_template('reg.html')






if __name__ == '__main__':
   # app.secret_key = os.urandom(12)
   app.secret_key = 'super secret key'

   app.run(debug = True)
