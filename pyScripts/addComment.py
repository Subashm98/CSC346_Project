#! /usr/bin/env python3
import cgi
import cgitb

import MySQLdb
from secret import secret

import os

cgitb.enable()

def style():
    print("""
    <style>
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
        
        .bg-gra-01 {
            background: linear-gradient(to top, #fbc2eb 0%, #a18cd1 100%); 
        }
        
        .bg-gra-02 {
            background: linear-gradient(to right, #F45C43, #EB3349); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        
            
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
            line-height: 50px;
            padding: 0 50px;
            transition: all 0.4s ease;
            cursor: pointer;
            font-size: 18px;
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
        input {
            outline: none;
            margin: 0;
            border: none;
            box-shadow: none;
            width: 100%;
            font-size: 14px;
            font-family: inherit;
        }
        
        .input--style-5 {
            line-height: 35px;
            background: #d2d4cb;
            height: 100px;
            width: 500px;
            box-shadow: inset 0px 1px 3px 0px rgba(0, 0, 0, 0.08);
        
            border-radius: 5px;
            padding: 0 20px;
            font-size: 16px;
            color: #666;
            transition: all 0.4s ease;
        }
        
        .label {
            font-size: 16px;
            color: #555;
            text-transform: capitalize;
            display: block;
            margin-bottom: 5px;
            margin-top: 5px;
        }
        
        .input-group {
            position: relative;
            margin-bottom: 22px;
        }
        
        .input-group-icon {
            position: relative;
        }
        

        
        /* ==========================================================================
            #TITLE
            ========================================================================== */
        .title {
            font-size: 24px;
            color: #525252;
            font-weight: 400;
            margin-bottom: 40px;
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
            padding: 57px 65px;
            padding-bottom: 65px;
        }
    </style>
    """)

def newCommentDiv(postId):
    print("""
    <br>
    <br>
    <div class="wrapper wrapper--w680">
        <div class="card card-4">
            <div class="card-body">
                <h2 class="title">Add a Comment<h2>
                <form method="POST" action="comment.py?post_id=%s">
                <div class="col-2">
                    <div class="row row-space">
                        <div class="input-group">
                                <label class="label">Comment</label>
                                <div class="input-group-icon">
                                    <textarea class="input--style-5" type="text" name="comment"  required></textarea>
                                </div>
                        </div>
                    </div>
                <div>
                    <div class="p-t-15">
                        <button class="btn btn--radius-2 btn--blue" type="submit">Add Comment</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <br>
    """%postId)

def addNewComment(postId):
    print("""
    <br>
    <br>
    <div class="page-wrapper bg-gra-02 font-poppins"> 
    """)

    newCommentDiv(postId)

    print("""</div>""")


def main():
    form = cgi.FieldStorage()
    postId  = form["post_id"].value
    print("<html>")
    print("<head>")
    print("<title>Discourse</title>")
    style()
    print("</head>")
    print("<body>")
    try:
        addNewComment(postId)
    except Exception as e:
        print(e)
    print("</body>")
    print("</html>")

    

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
    
    
    
    #print("""<h1>%s</h1>"""%postId)
    # if "comment" in form:
    #     comment = form["comment"].value
    #     cursor.execute("""INSERT INTO comment (post_id,user_name,msg_as_html)
    #                         VALUES (%s,%s,%s);""",
    #                         (postId,user, comment))

    #     cursor.close()
    #     conn.commit()
    #     conn.close()
        
    #     print("""<body onLoad="location.href='comment.py'"></body>""")
    # cursor.close()
    # conn.commit()
    # conn.close()

print("Content-Type: text/html;charset=utf-8")
print()
try:  
    main()
except Exception as e:
    print(e)
