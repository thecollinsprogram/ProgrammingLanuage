from lexer import *
from parser import *
from interpreter import *
import sys

file = open(sys.argv[1])
text = file.read()
file.close()

lexer = Lexer(text)
parser = Parser(lexer)
program = parser.program()
program.run()