from lexer import *
from parser import *
from ast import *

file = open("example.txt")
text = file.read()
file.close()

lexer = Lexer(text)

# while not lexer.eof:
# 	print(lexer.getNext())

parser = Parser(lexer)
ast = parser.program()
print(GLOBAL_SCOPE)