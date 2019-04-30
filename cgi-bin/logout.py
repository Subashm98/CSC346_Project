#! /usr/bin/env python3

import cgi

import cgitb
cgitb.enable()

import os
import sys

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

        cursor.execute("""DELETE FROM session WHERE sessionID = '%s'""" % token)
        conn.commit()
        cursor.close()
        conn.close()

        print("""<body onLoad="location.href='index.py'"></body>""")
                
    except:
        cursor.close()
        conn.close()
        print("""<body onLoad="location.href='index.py'"></body>""")


print("Content-Type: text/html")
print()
main()
