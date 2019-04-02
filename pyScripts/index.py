#! /usr/bin/env python3
import cgi
import cgitb
cgitb.enable()


print("Content-Type: text/html")
print("""
<html>
<head>
<title>Reddit</title>
</head>
<body>
   
        <div class="navigation-bar">
                <nav>
                        <ul id = "nav-ul">
                                <li id = "navLeft"><img id = "logo" src="http://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/logo.png"></li>
                                <li id = "navLeft"><a href="default.asp">Home</a></li>
                                <li id = "navLeft"><a href="news.asp">Contact</a></li>
                                <li id = "navRight"><img id = "userImg" src="https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/default_logImg.png"></li>
                               <!-- <li id = "navRight"><a href="contact.asp">Login</a></li> -->
                              <!--  <li id = "navRight"><a href="about.asp">Register</a></li> -->
                                <li id = "navRight">
                                        <form id = "loginForm" method ="POST">
                                                <!-- First name -->
                                                <input type="text"  placeholder="username" name="username">
                                                <!-- Last name -->
                                                <input type="password" placeholder  = "password" name="password">
                                                <input type="submit" id = "loginBtn" value="Login">
                                        </form>
                                </li>




                            
                    </ul>
                </nav>
                
        </div>
	<!-- <div class = "container"> </div> -->



</body>
</html>
 
""")


form = cgi.FieldStorage()


if 'loginForm' not in form:
        print(""" 
                <div class = "container">
                        <div class = "signUpInfo">
                                <h3>Sign up to experience the full glory of , where you can post new  content </h3>
                                <br>
                                <p>See what other people have posted</p>
                        </div>
                        <div class = "singUpForm">
                                <form id = "registerForm" method ="POST">
                                        <h2 id = "becomeMem">Register and become a member</h2>
                                        <!-- First name -->
                                        <input type="text"  id = "rInput" placeholder="first name" name="rfirstname">
                                        <!-- Last name -->
                                        <input type="text" id = "rInput" placeholder  = "last name " name="rlastname">
                                        <br>
                                        <input type="text" id = "rInputI" placeholder  = "username" name="rUsername">
                                        <br>
                                        <input type="password"  id = "rInputI" placeholder  = "password" name="lastname">
                                        <br>
                                        <input type="submit" id = "registerBtn" value="Register">
                                        
                                </form>                
                                
                                
                        </div>
        
        
                </div>
        """)       








# style the html
print("""

        <style>
                body {
                        /* background-color: lightgray; */
                        /* background-image: url("milkeyWay.jpeg"); */
                        /* background-image: url("backgrounds-blank-blue-953214.jpg");
                        background-image: url("backgrounds-blank-blue-953214.jpg"); */
                        background-image: url("abstract-art-artistic-1020315_C2.jpg");
                        margin: 0;
                        padding: 0;     
                }



       

        nav{
                width : 100%;
                height: 20%;
                overflow: auto;

        }

        #userImg{
                width : 50px;
                height: 35px;
                margin: 5px 5px 0px 5px;
        }

        .navigation-bar{
                top: 0;
                width: 100%;
                position : fixed; 
        

        
        }



        #logo{
                width : 60px;
                height: 50px;
                margin: 0px 0px 0px 0px;
                padding:0;
        }



        #nav-ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color:#56ABE4;

        }
        
        #nav-ul li {
        /* float: left; */
                margin: 0 0 -10px 0;
        }

        #navLeft{
                float : left;
        }

        #navRight {
        float : right;
        }
        
        #nav-ul li a {
                display: block;
                color: white;
                text-align: center;

                padding: 14px 16px;
                text-decoration: none;
        }

        #loginBtn{
                background-color: #56ABE4 ;
                border: none;
                color: white;
                padding: 10px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                /* margin: 4px 2px; */
                cursor: pointer;
        }

        #loginBtn:hover{
                background-color: red;
        }
        
        /* Change the link color to #111 (black) on hover */
        #nav-ul li a:hover {
                background-color: red;
        }

        .container{
                width : 80%;
                /* height: */
                margin-top: 45px;
                margin-left: 10%;
                margin-right: 10%;
                /* background-color: rgb(76, 99, 91); */
                background-image: url("abstract-attractive-backdrop-988872.jpg") 
        }

        .signUpInfo{
                background-color: lightgrey;
                border: solid red;
                margin : 20px;
                margin-right: 10%;
                margin-left: 10%;
                height: 100%;


        }
        .singUpForm{
                background-color: lightgrey;
                border: solid red;
                margin-right: 10%;
                margin-left: 10%;
                margin-bottom: 10%;
                height: 100%;

        }

        #rInput{
                width: 200px;
                font-size: 16px;
                padding: 25px;
                text-align: center;
                margin: 15px;

        }
        #rInputI{
                width: 480px;
                font-size: 16px;
                padding: 25px;
                text-align: center;
                margin: 20px;

        }

        #registerBtn{
                border: none;
                padding: 10px 32px;
                margin-left: 240px;
                margin-bottom: 20px;
                font-size: 16px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                background-color: lightblue;


        }

        #becomeMem{
                margin: 20px;
        }





	</style>

""")
#print(""" </body> </html> """")



