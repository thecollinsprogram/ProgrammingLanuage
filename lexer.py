from token import *

SYMBOLS = ["+", "-", "*", "/", "(", ")", "="]
KEYWORDS = ["var"]

class Lexer:
	
	def __init__(self, text):
		self.text = text
		self.pos = 0
		self.char = self.text[0]
		self.eof = False
		
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
			
		token = self.getNextIdentifier()
		if token:
			return token
			
		if self.eof:
			return Token("EOF", "EOF")
			
		self.error()
			
	def stripWhitespace(self):
		while self.char == " " or self.char == "\n":
			self.advance()
	
	def getNextNumber(self):
		if self.char.isdigit():
			number = self.char
			self.advance()
			
			while not self.eof and self.char.isdigit():
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
		
	def getNextIdentifier(self):
		if self.char.isalpha or self.char == "_":
			identifier = self.char
			self.advance()
			
			while not self.eof and self.char.isalpha() or self.char == "_" or self.char.isdigit():
				identifier += self.char
				self.advance()
			
			token = Token("IDEN", identifier)
				
			for keyword in KEYWORDS:
				if keyword == identifier:
					token = Token(keyword, keyword)
				
			return token
		else:
			return False
	
	def advance(self):
		self.pos += 1
		if self.pos < len(self.text):
			self.char = self.text[self.pos]
		else:
			self.eof = True