#! /usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

import os

from http import cookies

import MySQLdb
from secret import secret


def main():
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
            cursor.execute("""SELECT sessionID FROM session WHERE sessionID = '%s';""" % token)
            results = cursor.fetchall()

            tokenResults = [tok[0] for tok in results]

            if (token in tokenResults):
		cursor.execute("""DELETE FROM session WHERE sessionID = '%s'""" % token)
		conn.commit()
		cursor.close()
		conn.close()
		
            print("""<body onLoad="location.href='loginPage.py'"></body>""")
            
    except:
            print("""<body onLoad="location.href='loginPage.py'"></body>""")

print("Content-Type: text/html")
print()
main()
