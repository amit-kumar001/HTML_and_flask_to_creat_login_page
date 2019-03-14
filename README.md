# HTML_and_flask_to_creat_login_page
## Key feature
<ol>
<li>Create the login page <strong>(sigin.html)</strong> and registration page <strong>(reg.html)</strong> with the help of <strong>HTML language</strong>, only register user can enter in login page otherwise user have to fill details in the registration page to become register user.</li> </br> 
    
   ![sess2](https://user-images.githubusercontent.com/47202519/54346602-60bdb080-466b-11e9-8193-ee61015ba34f.png) </br></br> 
   ![sess1](https://user-images.githubusercontent.com/47202519/54346898-e4779d00-466b-11e9-9ef3-851c4db36a99.png)
    
  
<li>Create a database in <strong>phpmyadmin</strong> and make a connection with the registration page and login page with the help of flask,  when we enter details in to the registration page all details will store in the database.</li>
~~~

~~~
<li>post method is used to transfer user details into the database</li>

<li>in the form action attribute <form action="http://localhost:5000/index"> define server path with function name, this will use in .py page to call that same function</li>
<li>with the help of same function name we can store data from html page to database with the help of flask</li>
<li>back to main page (login page ) only register username and password can have access to enter in this page.</li>
<li>SQL query (SELECT count(1) FROM register WHERE username = %s;", [username]) is used to check that username is already store in the database if it exists in the database then enter password otherwise it will show error "check username"   </li>
<li>the last condition will be same to check the password, if enterd username and  password exist in the database then we can enter in the new page otherwise it will show error "please check username and password" </li>
</ol>  
