#!/usr/bin/python3

""" This module holds the base class for """
class Base:
	""" This serves as the base class on which the other classes will be built """
	__nb_objects = 0
	
	def __init__(self, id=None, __nb_objects = 0):
		if id != None:
			self.id = id
		else:
			Base.__nb_objects+=1
			self.id = Base.__nb_objects
