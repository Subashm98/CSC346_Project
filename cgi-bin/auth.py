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

def create_database():
	conn = MySQLdb.connect(host = secret.SQL_HOST,
        	               user = secret.SQL_USER,
                	       passwd = secret.SQL_PASSWD,
        	               db = secret.SQL_DB
	)

	user = 'user'
	post = 'post'
	comment = 'comment'

	cursor = conn.cursor()
	cursor.execute("""SHOW TABLES""")
	results = cursor.fetchall()

	results = [tabletuple[0] for tabletuple in results]
	
#
#	if (user not in results or post not in results or comment not in results):
#		cursor.execute("""CREATE TABLE user (
#				  user_id		VARCHAR (15) NOT NULL,
#				  first_name	VARCHAR (15) NOT NULL,
#				  last_name		VARCHAR (15) NOT NULL,
#				  pass_hash		VARCHAR (15) NOT NULL,
#				  gender		VARCHAR (7)  NOT NULL,
#				  email			VARCHAR (30) NOT NULL UNIQUE,
#				  phone_number	VARCHAR (11) NOT NULL,
#				  CONSTRAINT PK_USERS PRIMARY KEY (user_id)
#				  );
#				  """)

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
	
	
	if (user not in results):
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

	cursor.close()
	conn.close()
def main():
	print("<p>Hello</p>")

print("Content-Type:text/html")
print()
main()
