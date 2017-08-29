class Parser:
	
	def __init__(self, lexer):
		self.lexer = lexer
		self.token = self.lexer.getNext()
		
	def error(self):
		raise Exception("Unexpected token: " + self.token.value)
		
	def eat(self, type):
		if self.token.type == type:
			self.token = self.lexer.getNext()
		else:
			self.error()
		
	def factor(self):
		if self.token.type == "INT":
			value = self.token.value
			self.eat("INT")
			return value
			
		elif self.token.type == "(":
			self.eat("(")
			result = self.expr()
			self.eat(")")
			return result
			
		else:
			self.error()
	
	def term(self):
		result = self.factor()
		while self.token.type in ("*", "/"):
			if self.token.type == "*":
				self.eat("*")
				result = result * self.factor()
			elif self.token.type == "/":
				self.eat("/")
				result = result / self.factor()
				
		return result
				
		
	def expr(self):
		result = self.term()
		while self.token.type in ("+", "-"):
			if self.token.type == "+":
				self.eat("+")
				result = result + self.term()
			elif self.token.type == "-":
				self.eat("-")
				result = result - self.term()
				
		return result