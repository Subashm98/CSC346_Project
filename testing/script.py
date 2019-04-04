#! /usr/bin/env python3

import cgi

#enable debugging
import cgitb
cgitb.enable()

import MySQLdb
from secret import secret


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
#				  user_id	INT UNSIGNED NOT NULL AUTO_INCREMENT,
#				  first_name	VARCHAR (15) NOT NULL,
#				  last_name	VARCHAR (15) NOT NULL,
#				  pass_hash	VARCHAR (15) NOT NULL,
#				  gender	VARCHAR (7)  NOT NULL,
#				  email		VARCHAR (30) NOT NULL UNIQUE,
#				  phone_number	VARCHAR (11) NOT NULL,
#				  CONSTRAINT PK_USERS PRIMARY KEY (user_id)
#				  );
#				  """)

#		cursor.execute("""CREATE TABLE post (
#				  post_id	INT UNSIGNED NOT NULL AUTO_INCREMENT,
#				  user_id	INT NOT NULL,
#				  msg_as_html	VARCHAR (100) NOT NULL,
#				  CONSTRAINT PK_POST PRIMARY KEY (post_id),
#				  CONSTRAINT FK_USER_POST FOREIGN KEY (user_id) REFERENCES users (user_id)
#				  );
#				  """)

#		cursor.execute(CREATE TABLE comment (
#				  comment_id	INT UNSIGNED NOT NULL AUTO_INCREMENT
#				  post_id	INT NOT NULL,
#				  user_id	INT NOT NULL,
#				  msg_as_html	VARCHAR (100) NOT NULL
#				  CONSTRAINT PK_COMMENT PRIMARY KEY (comment_id),
#				  CONSTRAINT FK_COMMENT_POST FOREIGN KEY (post_id) REFERENCES post (post_id),
#				  CONSTRAINT FK_COMMENT_USER FOREIGN KEY (user_id) REFERENCES user (user_id)
#				  );
#				  """)
	
	
	if (user not in results):
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

	cursor.close()
	conn.close()


def main():
	form = cgi.FieldStorage()
	try:
		create_database()
	except Exception as e:
		print("<h1>Database connection not established, restart and try again</h1>")
		print(e)
		return

	print("""
		<form action = "login.py" method="POST">
		  First name: <input type="text" name="user_name">
		  Last name: <input type="text" name="full_name">
		  Password: <input type="password" name="password">
		  Email: <input type="text" name="email">
		  Gender: <input type="text" name="gender">
		  Phone number: <input type="text" name="phone">
		  
		  <input type="submit" value="Submit">
		</form>
		""")

	
print("Content-Type: text/html")
print()

main()
