#! /usr/bin/env python3

import cgi

import cgitb
cgitb.enable()

import MySQLdb
from secret import secret

def print_users(cursor):
	# cursor.execute("SELECT password FROM user;")
	# print(cursor.fetchall())
	# for account in cursor.fetchall():
	# 	print(account)
	# 	print("<hr>")
	x = "123"
	pwd = cursor.execute("""SELECT password FROM user WHERE user_name = %s;""" % x)
	pwd = pwd.fetchall()
	pwdResult = [ptuple[0] for ptuple in pwd]
	print(pwdResult)

def pHash(pword):
	# To be Implemented
	return pword


def main():
	form = cgi.FieldStorage()
	
	conn = MySQLdb.connect(host = secret.SQL_HOST,
        	               user = secret.SQL_USER,
                	       passwd = secret.SQL_PASSWD,
                       	db = secret.SQL_DB
	)

	try:
		cursor = conn.cursor()
		cursor.execute("""INSERT INTO user (user_name,full_name,password,gender,email,phone) 
							VALUES (%s,%s,%s,%s,%s,%s);""", 
							(form["user_name"].value, form["full_name"].value, 
							pHash(form["password"].value), form["gender"].value,
							form["email"].value, form["phone"].value))

		print_users(cursor)	

		cursor.close()
		conn.commit()
		
	except Exception as e:
		conn.rollback()
		print("<h1>An error has occured in adding to the database</h1>")
		print(e)	

	print("""<a href="./script.py">Back</a>""")

	conn.close()

print("Content-Type: text/html")
print()

main()
