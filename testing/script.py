#! /usr/bin/env python3

import cgi

#enable debugging
import cgitb
cgitb.enable(display=0, logdir="/var/log/httpd/cgi_err/")

print("Content-Type: text/html")
print()


form = cgi.FieldStorage()
if "firstname"  in form and "lastname" in form:
	print("""Your first name is %s and your last name is %s""" % (form["firstname"].value, form["lastname"].value))	
else:
	print("""
		<form>
		  First name: <input type="text" name="firstname">
		  Last name: <input type="text" name="lastname">
		  <input type="submit" value="Submit">
		</form>
		""")

