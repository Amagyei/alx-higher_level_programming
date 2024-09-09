#!/usr/bin/python3

""" function that checks if object is instance """

def is_same_class(obj, a_class):
	""" function that checks if object is instance """
	if issubclass(obj, a_class):
		return True
	else:
		return False
