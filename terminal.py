from lexer import *
from parser import *
from interpreter import *

command = input(">>> ")

while command != ".exit":

	lexer = Lexer(command)
	parser = Parser(lexer)
	program = parser.program()
	program.run()

	prompt = ""
	for name, var in GLOBAL_SCOPE.items():
		if callable(var):
			var = var()
		prompt += "(" + name + " : " + str(var) + ") "

	prompt = prompt + ">>> "
	command = input(prompt)