#! /usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

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
       /* 
        #FONT
        */
        .font-robo {
            font-family: "Roboto", "Arial", "Helvetica Neue", sans-serif;
        }
        
        .font-poppins {
            font-family: "Poppins", "Arial", "Helvetica Neue", sans-serif;
        }
        
        /* 
            #GRID
        */
        .row {
            display: flex;
            flex-wrap: wrap;
        } 
        html {
            box-sizing: border-box;
        }
        
        * {
            padding: 0;
            margin: 0;
        }
        
        *, *:before, *:after {
            box-sizing: inherit;
        }
        
        body,
        h1, h2, h3, h4, h5, h6,
        blockquote, p, pre,
        dl, dd, ol, ul,
        figure,
        hr,
        fieldset, legend {
            margin: 0;
            padding: 0;
        }
        
        li > ol,
        li > ul {
            margin-bottom: 0;
        }
        
        table {
            border-collapse: collapse;
            border-spacing: 0;
        }
        
        fieldset {
            min-width: 0;
            border: 0;
        }
        
        button {
            margin-top: 5px;
            outline: none;
            background: none;
            border: none;
        }
        
        /* ==========================================================================
            #PAGE WRAPPER
            ========================================================================== */
        .page-wrapper {
            min-height: 100vh;
        }
        
        body {
            font-family: "Poppins", "Arial", "Helvetica Neue", sans-serif;
            font-weight: 400;
            font-size: 14px;
        }
            
        /* ==========================================================================
            #WRAPPER
            ========================================================================== */
        .wrapper {
            margin: 0 auto;
        }
        
        .wrapper--w960 {
            max-width: 960px;
        }
        
        .wrapper--w780 {
            max-width: 780px;
        }
        
        .wrapper--w680 {
            max-width: 680px;
        }
        
        /* ==========================================================================
            #BUTTON
            ========================================================================== */
        .btn {
            display: inline-block;
            line-height: 25px;
            padding: 0 20px;
            transition: all 0.4s ease;
            cursor: pointer;
            font-size: 14px;
            color: #fff;
            font-family: "Poppins", "Arial", "Helvetica Neue", sans-serif;
        }
        
        .btn--radius {
            border-radius: 3px;
        }
        
        .btn--radius-2 {
        
            border-radius: 5px;
        }
            
        .btn--blue {
            background: #4272d7;
        }
        
        .btn--blue:hover {
            background: #2859c5;
        }
        
        
        /* 
            #FORM
        */
        
        
        .label {
            font-size: 16px;
            color: #555;
            text-transform: capitalize;
            display: block;
        }
        

        
        /* ==========================================================================
            #TITLE
            ========================================================================== */
        .title {
            font-size: 22px;
            color: #525252;
            font-weight: 400;
            margin-bottom: 10px;
        }
        
        /* 
            #CARD
        */
        .card {
            border-radius: 3px;
            background: #fff;
        }
        
        .card-4 {
            background: #fff;
            border-radius: 10px;
            box-shadow: 0px 8px 20px 0px rgba(0, 0, 0, 0.15);
        }
        
        .card-4 .card-body {
            padding: 40px 45px;
            padding-bottom: 20px;
        }
	p{
	    margin-left: 10px;
	} 


        </style>
        
        """)


def hNavBar(user):
        print("""
        <div class="navigation-bar">
                <nav>
                    <ul id = "nav-ul">
                            <li id = "navLeft"><img id = "logo" src="https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/logo.png"></li>
                            <li id = "navLeft"><a href="index.html">Home</a></li>
                            <li id = "navLeft"><a href="addPost.py">Add Post</a></li>
                            <li id = "navRight"><img id = "userImg" src="https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/default_logImg.png"></li>
                                       
                             <li id = "navRight">
                                <label for="uname" class="label">%s</label>
                            </li>


                            
                    </ul>
                </nav>
                
        </div>
        """ % user)

def showPost(title,op,cont,likes):
    print("""
    <br>
    <br>
    <div class="wrapper wrapper--w960">
        <div class="card card-4">
	    <div class="card-body">
	        <h4 class="title">%s , by:%s<h4>
		<hr>
		<form method="POST">
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
    """%(title,op,cont,likes))

def printPost():
    print("""
    <br>
    <br>
    <div class="page-wrapper font-poppins"> 
    """)
    for i in range(10):
    	showPost("title %s " % i,"user", " content %s " % i, i)


    print("""</div>""")


def main():
    form = cgi.FieldStorage()

    print("hello")

    for x in form:
        print("""<h1>form value: %s</h1>""" % x)

    # print("<html>")
    # print("<head>")
    # print("<title>Discourse</title>")
    # style()
    # print("</head>")
    # print("<body>")

    # conn = MySQLdb.connect(host = secret.SQL_HOST,
    #     	               user = secret.SQL_USER,
    #             	       passwd = secret.SQL_PASSWD,
    #                    	   db = secret.SQL_DB
	# )

    
    # user = "Subash" #form["uname"].value
    # hNavBar(user)
    # printPost()
    # #loginDiv()
    # #registerDiv()
    # print("</body>")
    # print("</html>")
print("Content-Type: text/html;charset=utf-8")
print()
main()


