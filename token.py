class Token:
	
	def __init__(self, type, value):
		self.type = type
		self.value = value
		
	def __str__(self):
		return "Type (" + self.type + ") : Value (" + str(self.value) + ")"
		
	def __rep__(self):
		return self.__str__()