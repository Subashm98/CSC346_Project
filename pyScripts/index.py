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
                            <li id = "navLeft"><img id = "logo" src="logo.png"></li>
                            <li id = "navLeft"><a href="default.asp">Home</a></li>
                            <li id = "navLeft"><a href="news.asp">Contact</a></li>
                            <li id = "navRight"><img id = "userImg" src="default_logImg.png"></li>
                            <li id = "navRight"><a href="contact.asp">Login</a></li>
                            <li id = "navRight"><a href="about.asp">Register</a></li>
                            
                    </ul>
                </nav>
                
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



        </style>

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

        ;
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


""")




print(""" </body> </html> """")




