#! /usr/bin/env python3


import cgi

print("Content-Type: text/html")
print()


form = cgi.FieldStorage()

if "username" in form:
	print("""<h1>Hello</h1>""")
if "password" in form:
	print("""<h1>%s</h1>""" % form["password"].value)

