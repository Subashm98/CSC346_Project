#! /usr/bin/env python3

import cgi

import cgitb
cgitb.enable()

import threading

import MySQLdb
from secret import secret

def main():
    form = cgi.FieldStorage()

    # if "disbtn" in form:
    #     print("<><><><><><><><><><><><><><>DisLike button was clicked<><<><><><><><><><><><><>")

    # if "cmbtn" in form:
    #     print("<><><><><><><><><><><><><><>Comment button was clicked<><<><><><><><><><><><><>")

    # if "likeBtn" in form:
    #     print("<><><><><><><><><><><><><><>Like button was clicked<><<><><><><><><><><><><>")

    idd = int(form["post_id"].value)

    conn = MySQLdb.connect(host = secret.SQL_HOST,
        	               user = secret.SQL_USER,
                	       passwd = secret.SQL_PASSWD,
                       	   db = secret.SQL_DB
	)

    cursor = conn.cursor()
    cursor.execute("""SELECT likes FROM post WHERE post_id = %s;""" % idd)
    results = cursor.fetchall()

    usrResult = [utuple[0] for utuple in results]
    
    user = usrResult[0]
    if "disbtn" in form:
        user = user - 1
    if "likeBtn" in form:
        user = user + 1

    if "cmbtn" in form:
        print("""<body onLoad="location.href='comment.py'"></body>""")

    cursor.execute("""UPDATE post SET likes = %s WHERE post_id = %s""", (user, idd))
    cursor.close()
    conn.commit()
    conn.close()

    print("""<body onLoad="location.href='index.py'"></body>""")


print("Content-Type:text/html")
print()
main()