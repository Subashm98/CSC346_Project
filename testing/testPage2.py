#! /usr/bin/env python3

import cgi

import cgitb
cgitb.enable()

import os
import sys

from http import cookies

def main():
	for item in os.environ.keys():
		print("""%s, %s<br>""" % (item, os.environ[item]))
	try:
		cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
		print("sessionID = " + cookie["session"].value)
	except Exception as e:
		print(e)
		print("cookie not set")

	if ("HTTP_COOKIE" not in os.environ):
		print("cookie not set 2")
	else:
		print("cookie set!!!")

	print("""<a href="./testPage3.py">TP3</a>""")

print("Content-Type: text/html")
print()
main()
