#! /usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

import os

import MySQLdb
from secret import secret


# style the html
def style():
        print("""
        <style>
        body {
                /* background-color: lightgray; */
                /* background-image: url("milkeyWay.jpeg"); */
                /* background-image: url("backgrounds-blank-blue-953214.jpg");
                background-image: url("backgrounds-blank-blue-953214.jpg"); */
                background-image: url("https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/abstract-art-artistic-1020315_C2.jpg");
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
        
        #nav-ul li a, label {
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
            width: 60px;
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
            margin: 5px;
    }


        </style>
        
        """)


def hNavBar(user):
        print("""
        <div class="navigation-bar">
                <nav>
                    <ul id = "nav-ul">
                            <li id = "navLeft"><img id = "logo" src="https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/logo.png"></li>
                            <li id = "navLeft"><a href="loginPage.py">Logout</a></li>
                            <li id = "navLeft"><a href="addPost.py">Add Post</a></li>
                            <li id = "navRight"><img id = "userImg" src="https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/default_logImg.png"></li>
                                       
                             <li id = "navRight">
                                <label for="uname" class="label">%s</label>
                            </li>


                            
                    </ul>
                </nav>
                
        </div>
        """ % user)

def showPost(idd, title,op,cont,likes):
    print("""
    <br>
    <br>
    <div class="wrapper wrapper--w960">
        <div class="card card-4">
	    <div class="card-body">
	        <h4 class="title">%s , by:%s<h4>
		<hr>
		<form method="POST" action=like.py>
                <input type = "hidden" name = "pname" value = \"%s\"></input>
          	    <div class="row row-space">
                        <div class="col-2">
                            <div class="input-group">
                                <label class="label">%s</label>
                            </div>
			   <p>%s likes</p>
                        </div>
                    </div>
                    <div class="p-t-15">
                    	<button class="btn btn--radius-2 btn--blue" type="submit">Like</button>
               	    </div>
        	</form>
	    </div>
        </div>
    </div>
    <br>
    """%(title,op,idd,cont,likes))

def printPost(cursor):
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
         showPost(post[0],post[1], post[2], post[3], post[4])

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
    cursor.execute("""SELECT user_name FROM sesh WHERE server_ip = \"%s\";""" % ip)
    results = cursor.fetchall()
    
    usrResult = [utuple[0] for utuple in results]
    
    user = usrResult[0]
    hNavBar(user)
    printPost(cursor)
    #loginDiv()
    #registerDiv()
    print("</body>")
    print("</html>")
print("Content-Type: text/html;charset=utf-8")
print()
main()


