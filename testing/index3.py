#! /usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

import os

from http import cookies

import MySQLdb
from secret import secret


# style the html
def style():
        print("""
        <style>
        body {
               /* background-image: url("https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/abstract-art-artistic-1020315_C2.jpg");*/
                /*background: linear-gradient(to right, #F45C43, #EB3349);*/
                /*background: linear-gradient(to top, #fbc2eb 0%, #a18cd1 100%); */
                background-color: #abe9cd;
                background-image: linear-gradient(315deg, #abe9cd 0%, #3eadcf 74%);

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

        #userImg{
            border-radius: 10px;
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
                /*background-color:#56ABE4;*/
                background-color: #bbf0f3;
                background-image: linear-gradient(315deg, #bbf0f3 0%, #f6d285 74%);

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
        
        #nav-ul li a, label {
                display: block;
                color: white;
                text-align: center;

                padding: 14px 16px;
                text-decoration: none;
        }


        
        /* Change the link color to #111 (black) on hover */
        #nav-ul li a:hover {
                /*background-color: red;*/
                background-color: red;
               /* background-image linear-gradient(315deg, #20bf55 0%, #01baef 74%);*/

        }

        .font-poppins {
            font-family: "Georgia", "Arial", "Helvetica Neue", sans-serif;
        }
        .wrapper {
            
            margin: 0 auto;
            background: #fff;
            border-radius: 10px;
            box-shadow: 0px 8px 20px 0px rgba(0, 0, 0, 0.15);
            border-radius: 10px;
            background: #fff;
            width : 60%;
            padding: 20px;

        }

        .btn{
            border-radius: 5px;
            line-height: 20px;
            width: 70px;
            padding:2px;
            transition: all 0.4s ease;
            cursor: pointer;
            font-size: 14px;
            color: #fff;
            font-family: "Poppins", "Arial", "Helvetica Neue", sans-serif;
        }

            
        .btn{
            background: #4272d7;
        }
        .btn:hover {
            background: #2859c5;
        }
        
        .container .box {
            border-radius: 10px; 
            width:100%; 
            /* margin:50px;  */
            display:table; 
        }  
        .container .box .box-row { 
                display:table-row; 
        }
        .container .box .box-cell {
            border-radius: 3px;
            display:table-cell; 
            /* width:50%;  */
            padding:15px; 
        }
        .container .box .box-cell.box1 { 
            background:rgb(228, 231, 187); 
            color:white; 
            text-align:justify;
            margin: 5px;
            width: 10%; 
        }
        .container .box .box-cell.box2 { 
            /* margin: 10px; */
            background:rgb(82, 213, 236); 
            text-align:justify; 
        }
        .container .box .box-cell.box3 { 
            /* margin: 10px; */
        
            background:rgb(84, 219, 190); 
            text-align:justify; 
            
        }
        .label {
                font-size: 16px;
                color: #555;
                text-transform: capitalize;
                display: block;
                /*margin: 5px;*/
        }
        </style>
        
        """)


def hNavBar(isLoggedIn, user, imgSrc):
        if (isLoggedIn):
                print("""
                <div class="navigation-bar">
                        <nav>
                            <ul id = "nav-ul">
                                    <li id = "navLeft"><img id = "logo" src="https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/logo.png"></li>
                                    <li id = "navLeft"><a href="loginPage.py">Logout</a></li>
                                    <li id = "navLeft"><a href="addPost.py">Add Post</a></li>
                                    <li id = "navRight"><img id = "userImg" src="%s"></li>
                                               
                                     <li id = "navRight">
                                        <label for="uname" class="label">%s</label>
                                    </li>


                                    
                            </ul>
                        </nav>
                        
                </div>
                """%(imgSrc,user))
        else:
                print("""
                <div class="navigation-bar">
                        <nav>
                            <ul id = "nav-ul">
                                    <li id = "navLeft"><img id = "logo" src="https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/logo.png"></li>
                                    <li id = "navLeft"><a href="loginPage.py">Login</a></li>
                            </ul>
                        </nav>
                        
                </div>
                """)

def showPost(isLoggedIn, idd, title,op,cont,likes,imgSrc):
    imgWidth = "80%"
    if imgSrc == "":
        imgSrc = "https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/transparentImg.png"
        imgWidth = "10%"

    if (isLoggedIn):
        print("""
            <br>
            <br>
            <div class="wrapper wrapper--w680">
                <div class="container"> 
                    <div class="box"> 
                        <div class="box-cell box3"> 
                            %s , by: %s
                        </div>
                        <div class="box-row"> 
                            <form method="POST" action="like.py">
                                <input type = "hidden" name = "pname" value = \"%s\"></input>
                                
                                <div class="box-cell box1"> 
                                        <label class="label">Likes:%s</label>
                                        <button class="btn" type="submit" name="likeBtn" value="like">Like</button>
                                        <br>
                                        <button class="btn" type="submit" name="disbtn" value="dislike">Dislike</button>   
                                </div> 
                                <div class="box-cell box2"> 
                                    %s
                                    <br> 
                                    <br>
                                    <img src="%s" width="%s">
                                       
                                </div>
                            </form>
                            <form method="POST" action="comment.py">
                                <input type = "hidden" name = "post_id" value = \"%s\"></input>
                                <input type = "hidden" name = "user_name" value = \"%s\"></input>
                                <div class="box-cell box1"> 
                                        <button class="btn" type="submit" name="cmbtn" value="comment">Comments</button>    
                                </div> 
                            </form>

                        </div>                 
                    </div> 
                </div>
            </div>   
                
            </div>
            <br>   
            """%(title,op, idd, likes, cont, imgSrc, imgWidth,idd,op))
        
    else:
        print("""
            <br>
            <br>
            <div class="wrapper wrapper--w680">
                <div class="container"> 
                    <div class="box"> 
                        <div class="box-cell box3"> 
                            %s , by: %s
                        </div>
                        <div class="box-row"> 
                            <form">
                                <input type = "hidden" name = "pname" value = \"%s\"></input>
                                
                                <div class="box-cell box1"> 
                                        <label class="label">Likes:%s</label>
                                        <button class="btn" type="submit" name="likeBtn" value="like">Like</button>
                                        <br>
                                        <button class="btn" type="submit" name="disbtn" value="dislike">Dislike</button>   
                                </div> 
                                <div class="box-cell box2"> 
                                    %s
                                    <br> 
                                    <br>
                                    <img src="%s" width="%s">
                                       
                                </div>
                            </form>
                            <form method="POST" action="comment.py">
                                <input type = "hidden" name = "post_id" value = \"%s\"></input>
                                <input type = "hidden" name = "user_name" value = \"%s\"></input>
                                <div class="box-cell box1"> 
                                        <button class="btn" type="submit" name="cmbtn" value="comment">Comments</button>    
                                </div> 
                            </form>

                        </div>                 
                    </div> 
                </div>
            </div>   
                
            </div>
            <br>   
            """%(title,op, idd, likes, cont, imgSrc, imgWidth,idd,op))

def printPost(isLoggedIn, cursor):
    print("""
    <br>
    <br>
    <div class="page-wrapper font-poppins"> 
    """)
    # for i in range(10):
    # 	showPost("title %s " % i,"user", " content %s " % i, i)

    cursor.execute("""SELECT * FROM post;""")
    results = cursor.fetchall()

    for post in results:
         showPost(isLoggedIn, post[0],post[1], post[2], post[3], post[5], post[4])

    print("""</div>""")


def main():
    form = cgi.FieldStorage()

    print("<html>")
    print("<head>")
    print("<title>Discourse</title>")
    style()
    print("</head>")
    print("<body>")

    ip = str(os.environ["SERVER_ADDR"])

    conn = MySQLdb.connect(host = secret.SQL_HOST,
        	               user = secret.SQL_USER,
                	       passwd = secret.SQL_PASSWD,
                       	   db = secret.SQL_DB
	)

    cursor = conn.cursor()

    try:
            cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
            token = cookie["session"].value

            # Check if a session already exists with the current token, delete the session and reload login page if so
            cursor.execute("""SELECT user_name FROM session WHERE sessionID = '%s';""" % token)
            results = cursor.fetchall()
            userResults = [usr[0] for usr in results]

            if (len(userResults) != 0):
                    user = userResults[0]

                    cursor.execute("""SELECT userImg FROM user WHERE user_name = \"%s\";""" %user)
                    results = cursor.fetchall()

                    userImgResults = [img[0] for img in results]
                    userImg = userImgResults[0]

                    hNavBar(True, user, userImg)
                    printPost(True, cursor)

            else:
                hNavBar(False, "", "")
                printPost(False, cursor)
            
    except:
            hNavBar(False, "", "")
            printPost(False, cursor)


    cursor.close()
    conn.commit()
    conn.close()

    print("</body>")
    print("</html>")
print("Content-Type: text/html;charset=utf-8")
print()
main()



			
