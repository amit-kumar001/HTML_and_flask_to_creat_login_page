# HTML_and_flask_to_create_login_page
## Key feature
<ol>
<li>Create the login page <strong>(sigin.html)</strong> and registration page <strong>(reg.html)</strong> with the help of <strong>HTML language</strong>, only register user can enter in login page otherwise user have to fill details in the registration page to become register user.</li> </br> 
    
   ![sess2](https://user-images.githubusercontent.com/47202519/54346602-60bdb080-466b-11e9-8193-ee61015ba34f.png)</br></br>
   ![sess1](https://user-images.githubusercontent.com/47202519/54346898-e4779d00-466b-11e9-9ef3-851c4db36a99.png)
    
  
<li>Create a database in <strong>phpmyadmin</strong> and make a connection with the registration page and login page with the help of flask, when we enter details in to the registration page all details will store in the database.</li>

~~~
import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", password="Server@123", database="joins")
print("connection successful")
cursor = db.cursor()

~~~

<li>We use <strong>form action attribute</strong> with server path <strong><form action="http://localhost:5000/index"></strong>it will define server path with function name <strong>index</strong>, this function will used in <strong>.py</strong> page (in python file)<strong>session.py</strong> to call the same function</li>
    
~~~
In html page
    <form action="http://localhost:5000/index" method="post">
~~~
~~~
@app.route('/index', methods = ['GET','POST'])
def index():
   return render_template('sigin.html')
~~~

<li><strong>post method</strong> is used to transfer user details into the database</li>

~~~
 if request.method == 'POST':
      name = request.form['name']
      l_name = request.form['l_name']
      username = request.form['username']
      password = request.form['password']
      address = request.form['address']
      phone = request.form['phone']
      email = request.form['email']
      pincode=request.form['pincode']

~~~

<li>Back to main page (login page)<strong>(sigin.html)</strong> only register username and password can have access to enter in this page.</li>
https://github.com/amit-kumar001/HTML_and_flask_to_create_login_page
~~~  
@app.route('/index', methods = ['GET','POST'])
def index():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      
~~~

<li><strong>SQL query</strong> <strong> (SELECT count(1) FROM register WHERE username = %s;", [username])</strong> is used to check that username is already store in the database if it exists in the database then enter password otherwise it will show error "check username"   </li>
<li>Same as the last condition we'll use the <strong>SQL query</strong> to check a correct <strong>password</strong>, if enterd username and  password exist in the database then we can enter in the new page otherwise it will show error "please check username and password" </li>

~~~
cursor.execute("SELECT count(1) FROM register WHERE username = %s;", [username])  
      if cursor.fetchone()[0]:
         cursor.execute("SELECT count(1) FROM register WHERE password = %s;", [password])
         if cursor.fetchone()[0]:
           return "thank you"
         else:
          return "Check password"
      else:
         return"check username and password"
~~~

</ol>  

### How to run this file
<ol>
    <li>First we need to run <strong>.py</strong> <strong>(session.py)</strong> file because it provide server to run the flask.</li></br>  
 
 ![3rdimg](https://user-images.githubusercontent.com/47202519/54352071-c9f6f100-4676-11e9-9af0-a1b5373582e7.png)</br>
 <li>Second step:- Now we can run <strong>.html</strong> <strong>(sigin.html)</strong> <strong>(reg.html)</strong> files. </li>

       
</ol>
