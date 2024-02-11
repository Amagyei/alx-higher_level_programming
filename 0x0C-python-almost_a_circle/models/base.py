#!/usr/bin/python3

def base(self):
	__nb_objects = 0
	
	def __init__(self, id=None):
		if id != None:
			self.id = id
		else:
			__nb_objects++
			self.id = __nb_objects
	

