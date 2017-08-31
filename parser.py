from ast import *

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
			
	def advance(self):
		self.token = self.lexer.getNext()
		
	def factor(self):
		token = self.token
		
		if token.type == "+" or token.type == "-":
			self.advance()
			node = UnaryOp(token, self.factor())
			return node
		
		elif token.type == "INT":
			self.advance()
			num = Num(token)
			return num
			
		elif token.type == "(":
			self.eat("(")
			result = self.expr()
			self.eat(")")
			return result
			
		else:
			node = self.var()
			return node
	
	def term(self):
		node = self.factor()
		while self.token.type in ("*", "/"):
			token = self.token
			self.advance()
			node = BinOp(node, token, self.factor())
				
		return node
		
	def expr(self):
		node = self.term()
		while self.token.type in ("+", "-"):
			token = self.token
			self.advance()
			node = BinOp(node, token, self.term())
				
		return node
		
	def var(self):
		node = Var(self.token)
		self.eat("IDEN")
		return node
		
	def program(self):
		program = Program()
		while not self.lexer.eof:
			statement = self.statement()
			program.children.append(statement)
		return program
			
	def statement(self):
		var = self.var()
		self.eat("=")
		expr = self.expr()
		return Statement(var, expr)