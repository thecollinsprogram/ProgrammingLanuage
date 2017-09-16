GLOBAL_SCOPE = {}

class BinOp:
	
	def __init__(self, left, op, right):
		self.left = left
		self.op = op
		self.right = right
		
	def evaluate(self):
		a = self.left.evaluate()
		b = self.right.evaluate()
		if self.op == "+":
			return a + b
		if self.op == "-":
			return a - b
		if self.op == "*":
			return a * b
		if self.op == "/":
			return a / b
		if self.op == "==":
			return a == b
		if self.op == "!=":
			return a != b
		if self.op == ">":
			return a > b
		if self.op == "<":
			return a < b
		if self.op == ">=":
			return a >= b
		if self.op == "<=":
			return a <= b
		
class UnaryOp:
	
	def __init__(self, op, expr):
		self.op = op
		self.expr = expr
		
	def evaluate(self):
		if self.op.type == "+":
			return + self.expr.evaluate()
		if self.op.type == "-":
			return - self.expr.evaluate()
		
class Num:
	
	def __init__(self, token):
		self.value = token.value
		
	def evaluate(self):
		return self.value
		
class Variable:
	
	def __init__(self, token):
		self.name = token.value
		
	def evaluate(self):
		if self.name in GLOBAL_SCOPE:
			var = GLOBAL_SCOPE[self.name]
			if callable(var):
				return var()
			else:
				return var
		else:
			raise Exception("Undefined variable " + self.name + "!")
		
class VariableAssign:
	
	def __init__(self, var, opr, expr):
		self.var = var
		self.opr = opr
		self.expr = expr
		
	def run(self):
		if self.opr == ":=":
			GLOBAL_SCOPE[self.var.name] = self.expr.evaluate
		else:
			GLOBAL_SCOPE[self.var.name] = self.expr.evaluate()

class IfStatment:
	
	def __init__(self, condition, ifstats, elsestats):
		self.condition = condition
		self.ifstats = ifstats
		self.elsestats = elsestats

	def run(self):
		if self.condition.evaluate():
			for line in self.ifstats:
				line.run()
		else:
			for line in self.elsestats:
				line.run()

class Loop:

	def __init__(self, condition, statements):
		self.condition = condition
		self.statements = statements

	def run(self):
		while self.condition.evaluate():
			for line in self.statements:
				line.run()

class Print:

	def __init__(self, expr):
		self.expr = expr

	def run(self):
		print(self.expr.evaluate())
		
class Program:
	
	def __init__(self):
		self.children = []
		
	def run(self):
		for child in self.children:
			child.run()