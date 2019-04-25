#! /usr/bin/env python3

import cgi

import cgitb
cgitb.enable()

#from passlib.hash import pbkdf2_sha256

import threading
import time

import os
import sys

from http import cookies
import secrets

import MySQLdb
from secret import secret


def create_database(conn):
	user_tbl = 'user'
	post_tbl = 'post'
	comment_tbl = 'comment'
	sesh_tbl = 'sesh'
	session_tbl = 'session'

	cursor = conn.cursor()
	cursor.execute("""SHOW TABLES;""")
	results = cursor.fetchall()

	all_tables = [tabletuple[0] for tabletuple in results]
	
	if (user_tbl not in all_tables):
		cursor.execute("""CREATE TABLE user (
						  user_name	VARCHAR (30) NOT NULL,
						  full_name	VARCHAR (30) NOT NULL,
						  password	VARCHAR (30) NOT NULL,
						  gender	VARCHAR (7)  NOT NULL,
						  email		VARCHAR (30) NOT NULL UNIQUE,
						  phone	    VARCHAR (12) NOT NULL,
						  userImg   VARCHAR (256),
						  CONSTRAINT PK_USER PRIMARY KEY (user_name)
						  );
						  """)

	if (post_tbl not in all_tables):
		cursor.execute("""CREATE TABLE post (
						  post_id		INT UNSIGNED NOT NULL AUTO_INCREMENT,
						  title			VARCHAR (30) NOT NULL,
						  user_name		VARCHAR (30) NOT NULL,
						  msg_as_html	VARCHAR (512) NOT NULL,
						  postImage     VARCHAR (256) NOT NULL,
						  likes			INT	UNSIGNED NOT NULL,
						  CONSTRAINT PK_POST PRIMARY KEY (post_id),
						  CONSTRAINT FK_USER_POST FOREIGN KEY (user_name) REFERENCES user (user_name)
						  );
						  """)

	if (comment_tbl not in all_tables):
		cursor.execute("""CREATE TABLE comment (
						comment_id	INT UNSIGNED NOT NULL AUTO_INCREMENT,
						post_id		INT UNSIGNED NOT NULL,
						user_name	VARCHAR (30) NOT NULL,
						msg_as_html	VARCHAR (256) NOT NULL,
						CONSTRAINT PK_COMMENT PRIMARY KEY (comment_id),
						CONSTRAINT FK_COMMENT_POST FOREIGN KEY (post_id) REFERENCES post (post_id),
						CONSTRAINT FK_COMMENT_USER FOREIGN KEY (user_name) REFERENCES user (user_name)
						);
						""")

	if (sesh_tbl not in all_tables):
		cursor.execute("""CREATE TABLE sesh (
						server_ip	VARCHAR (30) NOT NULL,
						user_name	VARCHAR (30) NOT NULL,
						CONSTRAINT PK_SESH PRIMARY KEY (server_ip),
						CONSTRAINT FK_SESH_USER FOREIGN KEY (user_name) REFERENCES user (user_name)
						);
						""")

	if (session_tbl not in all_tables):
		cursor.execute("""CREATE TABLE session (
						sessionID	VARCHAR (30) NOT NULL,
						user_name	VARCHAR (30) NOT NULL,
						CONSTRAINT PK_SESSION PRIMARY KEY (sessionID),
						CONSTRAINT FK_SESSIONUSER FOREIGN KEY (user_name) REFERENCES user (user_name)
						);
						""")

	cursor.close()


def pHash(password):
	#To be Implemented
	return password



def gotoPage(pageName):
	print("""<body onLoad="location.href='%s'"></body>""" % pageName)
	sys.exit(0)


def delayPage(sec, pageName):
	threading.Timer(sec, gotoPage, [pageName]).start()


def update_user(cursor, user, token):
	# Code for IP
	ip = os.environ["SERVER_ADDR"]
	try:
		cursor.execute("""INSERT INTO sesh (server_ip,user_name)
						VALUES (%s,%s);""",
						(str(ip), user))
	except:
		cursor.execute("""DELETE FROM sesh WHERE server_ip = \"%s\";""" % ip)
		cursor.execute("""INSERT INTO sesh (server_ip,user_name)
					VALUES (%s,%s);""",
					(str(ip), user))

	# Code for cookies
	cursor.execute("""INSERT INTO session (sessionID, user_name)
					VALUES (%s,%s);""",
					(token, user))
		

def createCookie():
	cookie =  cookies.SimpleCookie()
	token = secrets.token_hex(15)
	cookie["session"] = token
	print(cookie)
	return token


def main():
	token = createCookie()
	print()
	
	form = cgi.FieldStorage()

	conn = MySQLdb.connect(host = secret.SQL_HOST,
        	               user = secret.SQL_USER,
                	       passwd = secret.SQL_PASSWD,
                       	   db = secret.SQL_DB
	)

	create_database(conn)
	cursor = conn.cursor()


	# Check if a session already exists with the current token, delete the session and reload login page if so
	cursor.execute("""SELECT sessionID FROM session;""")
	results = cursor.fetchall()
	
	tokenResults = [tok[0] for tok in results]
	
	if (token in tokenResults):
		cursor.execute("""DELETE FROM session WHERE sessionID = '%s'""" % token)
		conn.commit()
		cursor.close()
		conn.close()
		print("<h1>DUPLICATE TOKEN DETECTED, REDIRECTING BACK TO LOGIN PAGE</h1>")
		delayPage(5, "loginPage2.py")
		return


	# User Login
	if(form.getvalue("uname") and form.getvalue("psw")):
		cursor.execute("""SELECT password FROM user WHERE user_name = \"%s\";""" % form["uname"].value)
		results = cursor.fetchall()

		pwdResult = [ptuple[0] for ptuple in results]

		# Username does not exist
		if (len(pwdResult) == 0):
			cursor.close()
			conn.close()
			
			print("<h1>Bad Login, redirecting back to login page...</h1>")
			delayPage(2, "loginPage2.py")
			return
			

		#try:
		# Password is correct
		if(form["psw"].value == pwdResult[0]):
			update_user(cursor, form["uname"].value, token)
			conn.commit()

			cursor.close()
			conn.close()
				
			#gotoPage("index.py")
			gotoPage("testPage2.py")
			return

		# Password doesn't match with username
		else:
			cursor.close()
			conn.close()
			
			print("<h1>Bad Login, redirecting back to login page...</h1>")
			delayPage(2, "loginPage2.py")

		#except:
		#	cursor.close()
		#	conn.close()
		#	
		#	print("<h1>Bad Login, redirecting back to login page...</h1>")
		#	delayPage(2, "loginPage2.py")

	# registering a new user
	else: 
		try:
			userImg  = ""
			defaultImgURL = "https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/default_logImg.png"
			if "userImg" in form:
				userImg = form["userImg"].value
			else:
				userImg = defaultImgURL

			cursor.execute("""INSERT INTO user (user_name,full_name,password,gender,email,phone,userImg) 
							VALUES (%s,%s,%s,%s,%s,%s, %s);""", 
							(form["user_name"].value, form["full_name"].value, 
							pHash(form["password"].value), form["gender"].value,
							form["email"].value, form["phone"].value, userImg))
			
			update_user(cursor, form["user_name"].value, token)
			cursor.close()
			conn.commit()
			conn.close()

			#gotoPage("index.py")
			gotoPage("testPage2.py")
			return
			
		except Exception as e:
			print(e)
			conn.rollback()
			cursor.close()
			conn.close()
			
			print("<h1>Username or Email Taken, redirecting back to login page...</h1>")
			delayPage(2, "loginPage2.py")


print("Content-Type:text/html")
main()
