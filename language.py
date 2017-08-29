from lexer import *
from parser import *

text = input("==> ")
lexer = Lexer(text)
parser = Parser(lexer)
print(parser.expr())