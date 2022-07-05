#!/usr/bin/python3
"""
This function appends a string at the end of a text file (UTF8) and returns the number of characters added
"""

def append_write(filename="", text=""):
	"""The append_write module"""
	with open(filename, 'a') as f:
        	return f.write(text)
