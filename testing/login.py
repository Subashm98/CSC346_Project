#! /usr/bin/env python3

import cgi

import cgitb
cgitb.enable()

import MySQLdb

print("Content-Type: text/html")
print()


form = cgi.FieldStorage()


conn = MySQLdb.connect(host = "csc346-db.cszwdclaffoa.us-east-1.rds.amazonaws.com",
		       user = "CSC346_SC",
		       passwd = "S123456789C",
		       db = "csc346db")

cursor = conn.cursor()
cursor.execute("""INSERT INTO users(username,password) VALUES(%s,%s);""", (form["username"].value, form["password"].value))
cursor.close()

conn.commit()

if "username" in form:
	print("""<h1>Hello</h1>""")
if "password" in form:
	print("""<h1>%s</h1>""" % form["password"].value)


cursor = conn.cursor()
cursor.execute("SELECT * FROM users;")

print("<br><br><h2>List of accounts:</h2>")
print("<ul>")

for account in cursor.fetchall():
		print("<li> user:%s , pass:%s </li>" % (account[0],account[1]))

print("</ul>")

cursor.close()

print("""<a href="http://ec2-34-238-122-238.compute-1.amazonaws.com/cgi-bin/script.py">Back</a>""")

conn.close()
