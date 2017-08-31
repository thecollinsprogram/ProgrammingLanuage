GLOBAL_SCOPE = {}

class BinOp:
	
	def __init__(self, left, op, right):
		self.left = left
		self.op = op
		self.right = right
		
	def run(self):
		a = self.left.run()
		b = self.right.run()
		if self.op.type == "+":
			return a + b
		if self.op.type == "-":
			return a - b
		if self.op.type == "*":
			return a * b
		if self.op.type == "/":
			return a / b
		
class UnaryOp:
	
	def __init__(self, op, expr):
		self.op = op
		self.expr = expr
		
	def run(self):
		if self.op.type == "+":
			return +self.expr.run()
		if self.op.type == "-":
			return -self.expr.run()
		
class Num:
	
	def __init__(self, token):
		self.value = token.value
		
	def run(self):
		return self.value
		
class Var:
	
	def __init__(self, token):
		self.name = token.value
		
	def run(self):
		return GLOBAL_SCOPE[self.name]
		
class Statement:
	
	def __init__(self, var, expr):
		self.var = var
		self.expr = expr
		
	def run(self):
		value = self.expr.run()
		GLOBAL_SCOPE[self.var.name] = value
		
class Program:
	
	def __init__(self):
		self.children = []
		
	def run(self):
		for child in self.children:
			child.run()