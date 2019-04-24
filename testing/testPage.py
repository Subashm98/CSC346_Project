#! /usr/bin/env python3

import cgi

import cgitb
cgitb.enable()

import os
import sys

from http import cookies

def main():
        #try:
	cookie = cookies.SimpleCookie()
	cookie["session"] = "123"
	print(cookie)
	print()

	for item in os.environ.keys():
		print("""%s, %s<br>""" % (item, os.environ[item]))
		
	#print("""<a href="./testPage2.py">TP2</a>""")	
	
	print("""<body onLoad="location.href='./testPage2.py'"></body>""")

	#cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
                #print("sessionID = " + cookie["session"].value)
        #except Exception as e:
                #print(e)
                
print("Content-Type: text/html")
main()
