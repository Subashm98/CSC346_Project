#! /usr/bin/env python3

import cgi

import cgitb
cgitb.enable()

import os

from http import cookies

def main():
        try:
                cookie = cookies.SimpleCookie(os.environ["HTTP_COOOKIE"])
                print("sessionID = " + cookie["session"].value)
        except Exception as e:
                print(e)
                
print("Content-Type:text/plain")
print()
main()
