#! /usr/bin/env python3

import cgi

import cgitb
cgitb.enable()

import threading

import MySQLdb
from secret import secret

def main():
    form = cgi.FieldStorage()
    idd = int(form["pname"].value)

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
    user = user + 1

    cursor.execute("""UPDATE post SET likes = %s WHERE post_id = %s""", (user, idd))
    cursor.close()
    conn.commit()
    conn.close()

    print("""<body onLoad="location.href='index.py'"></body>""")


print("Content-Type:text/html")
print()
main()