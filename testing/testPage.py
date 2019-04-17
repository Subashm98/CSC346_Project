#! /usr/bin/env python3

import cgi

import cgitb
cgitb.enable()

import os

from http import cookies

print("Content-type: text/plain")

try:
    cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print("session = " + cookie["session"].value)
except (cookies.CookieError, KeyError):
    print("session cookie not set!")
