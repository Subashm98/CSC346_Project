#! /usr/bin/env python3

import cgi

import cgitb
cgitb.enable()

#from passlib.hash import pbkdf2_sha256

import MySQLdb
from secret import secret

def main():
	num = 123
	al  = "como"
	p = "hello"
	u  = "hello"
	#form = cgi.FieldStorage()
	form = cgi.FieldStorage()
	if(form.getvalue("uname") and form.getvalue("psw")):
		if(form["uname"].value == u and form["psw"].value == p):
			print("""<body onLoad="location.href='index.py'"><h1>Hurray you got in</h1>""")
			#execfile("loginPage.py")
			#print("""<p onLoad="index.py"></p>""")			
		else:
			print("""<body onLoad="location.href='loginPage.py'"></body>""")
			print("<h1>Wrong</h1>")
	else:
		print("<h1>OH NO something went wrong</h1>")

def create_database(conn):
	user_tbl = 'user'
	post_tbl = 'post'
	comment_tbl = 'comment'

	cursor = conn.cursor()
	cursor.execute("""SHOW TABLES""")
	results = cursor.fetchall()

	results = [tabletuple[0] for tabletuple in results]
	

#	if (user_tbl not in results or post_tbl not in results or comment_tbl not in results):
	if (user_tbl not in results):
		cursor.execute("""CREATE TABLE user (
				  user_id	INT UNSIGNED AUTO_INCREMENT,
				  first_name	VARCHAR (15) NOT NULL,
				  last_name	VARCHAR (15) NOT NULL,
				  pass_hash	VARCHAR (15) NOT NULL,
				  gender	VARCHAR (7)  NOT NULL,
				  email		VARCHAR (30) NOT NULL UNIQUE,
				  phone_number	VARCHAR (11) NOT NULL,
				  CONSTRAINT PK_USER PRIMARY KEY (user_id)
				  );
				  """)

#		cursor.execute("""CREATE TABLE post (
#				  post_id		INT UNSIGNED NOT NULL AUTO_INCREMENT,
#				  user_id		INT NOT NULL,
#				  msg_as_html	VARCHAR (256) NOT NULL,
#				  CONSTRAINT PK_POST PRIMARY KEY (post_id),
#				  CONSTRAINT FK_USER_POST FOREIGN KEY (user_id) REFERENCES users (user_id)
#				  );
#				  """)

#		cursor.execute(CREATE TABLE comment (
#				  comment_id	INT UNSIGNED NOT NULL AUTO_INCREMENT
#				  post_id		INT NOT NULL,
#				  user_id		INT NOT NULL,
#				  msg_as_html	VARCHAR (256) NOT NULL
#				  CONSTRAINT PK_COMMENT PRIMARY KEY (comment_id),
#				  CONSTRAINT FK_COMMENT_POST FOREIGN KEY (post_id) REFERENCES post (post_id),
#				  CONSTRAINT FK_COMMENT_USER FOREIGN KEY (user_id) REFERENCES user (user_id)
#				  );
#				  """)
	
	


	cursor.close()

def pHash(passwrord):
	#To be Implemented
	return password

def main2():
	form = cgi.FieldStorage()

	conn = MySQLdb.connect(host = secret.SQL_HOST,
        	               user = secret.SQL_USER,
                	       passwd = secret.SQL_PASSWD,
                       	db = secret.SQL_DB
	)

	create_database(conn)

	try:
		cursor = conn.cursor()
		cursor.execute("""INSERT INTO user (first_name,last_name,pass_hash,gender,email,phone_number) 
				  VALUES (%s,%s,%s,%s,%s,%s);""", 
				(form["first_name"].value, form["last_name"].value, 
				 pHash(form["password"].value), form["gender"].value,
				 form["email"].value, form["phone_number"].value))

		cursor.close()
		conn.commit()
		
	except Exception as e:
		conn.rollback()
		print("<h1>An error has occured in adding to the database</h1>")
		print(e)	

	print("""<a href="./script.py">Back</a>""")

	conn.close()

print("Content-Type:text/html")
print()
main()
