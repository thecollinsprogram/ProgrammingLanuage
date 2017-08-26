from lexer import *

KEYWORDS = []
SYMBOLS = ["==", "!=", "<=", ">=", "+=", "-=", "*=", "/=", "%=", "^=", "+", "-", "*", "/", "^", "%", "=", "!", "<", ">", ",", ".", "(", ")", "[", "]"]

file = open("example.txt")
text = file.read()
file.close()
tokens = lex(text, KEYWORDS, SYMBOLS)

for token in tokens:
	print(token.name + " : " + token.value)