from token import *

SYMBOLS = ["+", "-", "*", "/", "(", ")"]

class Lexer:
	
	def __init__(self, text):
		self.text = text
		self.pos = 0
		self.char = self.text[0]
		
	def error(self):
		raise Exception("Invalid character: " + self.char)
		
	def getNext(self):
		self.stripWhitespace()
		
		token = self.getNextNumber()
		if token:
			return token
			
		token = self.getNextSymbol()
		if token:
			return token
			
		if self.eof():
			return Token("EOF", "EOF")
			
		self.error()
			
	def stripWhitespace(self):
		while self.char == " ":
			self.advance()
	
	def getNextNumber(self):
		if self.char.isdigit():
			number = self.char
			self.advance()
			
			if not self.eof() and self.char.isdigit():
				number += self.char
				self.advance()
		
			return Token("INT", int(number))
		else:
			return False
			
	def getNextSymbol(self):
		for symbol in SYMBOLS:
			if symbol == self.char:
				self.advance()
				return Token(symbol, symbol)
		return False
		
	def eof(self):
		return self.char == "EOF"
	
	def advance(self):
		self.pos += 1
		if self.pos < len(self.text):
			self.char = self.text[self.pos]
		else:
			self.char = "EOF"