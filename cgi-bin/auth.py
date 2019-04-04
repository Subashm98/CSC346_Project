#! /usr/bin/env python3

import cgi

import cgitb
cgitb.enable()

#from passlib.hash import pbkdf2_sha256

import MySQLdb
from secret import secret

# def main():
# 	num = 123
# 	al  = "como"
# 	p = "hello"
# 	u  = "hello"
# 	#form = cgi.FieldStorage()
# 	form = cgi.FieldStorage()
# 	if(form.getvalue("uname") and form.getvalue("psw")):
# 		if(form["uname"].value == u and form["psw"].value == p):
# 			print("""<body onLoad="location.href='index.py'"><h1>Hurray you got in</h1>""")
# 			#execfile("loginPage.py")
# 			#print("""<p onLoad="index.py"></p>""")			
# 		else:
# 			print("""<body onLoad="location.href='loginPage.py'"></body>""")
# 			print("<h1>Wrong</h1>")
# 	else:
# 		print("<h1>OH NO something went wrong</h1>")

def create_database(conn):
	user_tbl = 'user'
	post_tbl = 'post'
	comment_tbl = 'comment'

	cursor = conn.cursor()
	cursor.execute("""SHOW TABLES;""")
	results = cursor.fetchall()

	all_tables = [tabletuple[0] for tabletuple in results]
	

#	if (user_tbl not in results or post_tbl not in results or comment_tbl not in results):
#		cursor.execute("DROP TABLE user;")
#		cursor.execute("DROP TABLE post;")
#		cursor.execute("DROP TABLE comment;")
	if (user_tbl not in all_tables):
		cursor.execute("""CREATE TABLE user (
				  user_name	VARCHAR (30) NOT NULL,
				  full_name	VARCHAR (30) NOT NULL,
				  password	VARCHAR (30) NOT NULL,
				  gender	VARCHAR (7)  NOT NULL,
				  email		VARCHAR (30) NOT NULL UNIQUE,
				  phone	VARCHAR (12) NOT NULL,
				  CONSTRAINT PK_USER PRIMARY KEY (user_name)
				  );
				  """)

#		cursor.execute("""CREATE TABLE post (
#				  post_id		INT UNSIGNED NOT NULL AUTO_INCREMENT,
#				  user_name		INT NOT NULL,
#				  msg_as_html	VARCHAR (256) NOT NULL,
#				  CONSTRAINT PK_POST PRIMARY KEY (post_id),
#				  CONSTRAINT FK_USER_POST FOREIGN KEY (user_name) REFERENCES user (user_name)
#				  );
#				  """)

#		cursor.execute(CREATE TABLE comment (
#				  comment_id	INT UNSIGNED NOT NULL AUTO_INCREMENT
#				  post_id		INT NOT NULL,
#				  user_name		INT NOT NULL,
#				  msg_as_html	VARCHAR (256) NOT NULL
#				  CONSTRAINT PK_COMMENT PRIMARY KEY (comment_id),
#				  CONSTRAINT FK_COMMENT_POST FOREIGN KEY (post_id) REFERENCES post (post_id),
#				  CONSTRAINT FK_COMMENT_USER FOREIGN KEY (user_name) REFERENCES user (user_name)
#				  );
#				  """)

	cursor.close()

def pHash(password):
	#To be Implemented
	return password

def main():
	form = cgi.FieldStorage()

	conn = MySQLdb.connect(host = secret.SQL_HOST,
        	               user = secret.SQL_USER,
                	       passwd = secret.SQL_PASSWD,
                       	   db = secret.SQL_DB
	)

	create_database(conn)
	cursor = conn.cursor()

	if(form.getvalue("uname") and form.getvalue("psw")):
		cursor.execute("""SELECT password FROM user WHERE user_name = %s;""" % form["uname"].value)
		results = cursor.fetchall()

		pwdResult = [ptuple[0] for ptuple in results]

		if(form["psw"].value == pwdResult[0]):
			print("""<body onLoad="location.href='index.py'"><h1>Hurray you got in</h1>""")	
		else:
			cursor.close()
			conn.close()
			print("<h1>Username and password or password is invalid</h1>")
			print("""<body onLoad="location.href='loginPage.py'"></body>""")
	else:
		try:
			cursor.execute("""INSERT INTO user (user_name,full_name,password,gender,email,phone) 
							VALUES (%s,%s,%s,%s,%s,%s);""", 
							(form["user_name"].value, form["full_name"].value, 
							pHash(form["password"].value), form["gender"].value,
							form["email"].value, form["phone"].value))

			cursor.close()
			conn.commit()
			conn.close()

			print("""<body onLoad="location.href='index.py'"></body>""")
			
		except Exception as e:
			conn.rollback()
			cursor.close()
			conn.close()
			print("<h1>Duplicate username found in database</h1>")
			print(e)
			#print("""<body onLoad="location.href='loginPage.py'"></body>""")


print("Content-Type:text/html")
print()
main()
