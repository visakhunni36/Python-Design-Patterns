

# The Factory Pattern

class Person:
	def __init__(self):
		self.name = name
		self.gender = gender
		
	def getName(self):
		return self.name
		
	def getGender(self):
		return self.gender
	


class Male(Person):
	def __init__(self, name):
		self.gender = 'male'
		self.name = name
		print('Hello Mr.'+name)
		

class Female(Person):
	def __init__(self, name):
		self.gender = 'female'
		self.name = name
		print('Hello Miss.'+name)
		

class Factory:
	def getPerson(self, name, gender):
		if gender == 'male':
			return Male(name)
		else:
			return Female(name)
		























































































































































