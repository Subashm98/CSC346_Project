#! /usr/bin/env python3


import cgi
import cgitb
cgitb.enable()
#from passlib.hash import pbkdf2_sha256

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

	adasd

print("Content-Type:text/html")
print()
main()
