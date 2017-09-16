from interpreter import *

class Parser:
	
	def __init__(self, lexer):
		self.lexer = lexer
		self.token = self.lexer.getNext()
		
	def error(self):
		raise Exception("Unexpected token '" + str(self.token.value) + "' on line " + str(self.lexer.line))
		
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
			result = self.condition()
			self.eat(")")
			return result
			
		else:
			node = self.variable()
			return node
	
	def term(self):
		node = self.factor()
		while self.token.type in ("*", "/"):
			type = self.token.type
			self.advance()
			node = BinOp(node, type, self.factor())
				
		return node
		
	def expr(self):
		node = self.term()
		while self.token.type in ("+", "-"):
			type = self.token.type
			self.advance()
			node = BinOp(node, type, self.term())
				
		return node

	def condition(self):
		node = self.expr()
		while self.token.type in (">", "<", "=", "!"):
			type = self.token.type
			self.advance()
			if self.token.type == "=":
				type += "="
				self.advance()
			if type == "!":
				self.error()
			node = BinOp(node, type, self.term())

		return node
		
	def variable(self):
		node = Variable(self.token)
		self.eat("IDEN")
		return node
		
	def program(self):
		program = Program()
		while not self.lexer.eof():
			statement = self.statement()
			program.children.append(statement)
		return program

	def block(self):
		if self.token.type == "{":
			statments = []
			self.eat("{")
			while self.token.type != "}":
				stat = self.statement()
				statments.append(stat)
			
			self.eat("}")
			return statments
			
		else:
			return [self.statement()]
			
	def statement(self):
		if self.token.type == "if":
			self.eat("if")
			condition = self.condition()
			ifstats = self.block()
			elsestats = []

			if self.token.type == "else":
				self.eat("else")
				elsestats = self.block()

			return IfStatment(condition, ifstats, elsestats)

		elif self.token.type == "while":
			self.eat("while")
			condition = self.condition()
			statements = self.block()
			return Loop(condition, statements)

		elif self.token.type == "print":
			self.eat("print")
			expr = self.condition()
			return Print(expr)

		else:
			var = self.variable()

			if self.token.type == "=":
				self.advance()
				opr = "="
			elif self.token.type == ":":
				self.advance()
				self.advance()
				opr = ":="
			else:
				self.error()

			expr = self.condition()
			return VariableAssign(var, opr, expr)