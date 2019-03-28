#! /usr/bin/env python3

print("Content-Type: text/html")
print()

print("This is the first line of the text file. Did you notice how we")
print("printed two lines above this? Those are for communicating with")
print("the Apache web server, telling it the type of the file that we")
print("are giving it.")
print()
print("Can you modify this script so that it generates a file of type")
print("text/html instead? And then could you change the contents so that")
print("this is a simple webpage instead?")


print("Content-Type: text/html")
print()

f = open("test.html", "r")

print(f.read())

f.close()
