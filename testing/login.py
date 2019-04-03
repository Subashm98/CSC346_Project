#! /usr/bin/env python3

import cgi

import cgitb
cgitb.enable()

import MySQLdb
from secret import secret

def print_users(cursor):
	cursor.execute("SELECT * FROM user;")
	for account in cursor.fetchall():
		print(account)
		print("<br>")

def pHash(password):
	# To be Implemented
	return password


def main():
	form = cgi.FieldStorage()
	
	conn = MySQLdb.connect(host = secret.SQL_HOST,
        	               user = secret.SQL_USER,
                	       passwd = secret.SQL_PASSWD,
                       	db = secret.SQL_DB
	)

	try:
		cursor = conn.cursor()
		cursor.execute("""INSERT INTO user (first_name,last_name,pass_hash,gender,email,phone_number) 
				  VALUES (%s,%s,%s,%s,%s,%s);""", 
				(form["first_name"].value, form["last_name"].value, 
				 pHash(form["password"].value), form["gender"].value,
				 form["email"].value, form["phone_number"].value))

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
