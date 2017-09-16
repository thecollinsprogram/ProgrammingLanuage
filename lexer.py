from token import *

SYMBOLS = ["+", "-", "*", "/", "(", ")", "=", ":", ">", "<", "!", "{", "}"]
KEYWORDS = ["if", "else", "while", "print"]

class Lexer:
	
	def __init__(self, text):
		self.text = text
		self.index = 0
		self.char = self.text[0]
		self.line = 1

	def error(self):
		raise Exception("Invalid character '" + self.char + "' on line " + str(self.line))
		
	def getNext(self):
		self.stripWhitespace()
		
		token = self.getNextNumber()
		if token:
			# print(token)
			return token
			
		token = self.getNextSymbol()
		if token:
			# print(token)
			return token
			
		token = self.getNextIdentifier()
		if token:
			# print(token)
			return token

		if self.eof():
			return Token("EOF", "EOF")
			
		self.error()
			
	def stripWhitespace(self):
		while self.char == " " or self.char == "\n" or self.char == "\t":
			if self.eof():
				break
			if self.char == "\n":
				self.line += 1
			self.advance()
	
	def getNextNumber(self):
		if self.char.isdigit():
			number = self.char
			self.advance()
			
			while not self.eof() and self.char.isdigit():
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
			
			while not self.eof() and self.char.isalpha() or self.char == "_" or self.char.isdigit():
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
		self.index += 1
		if not self.eof():
			self.char = self.text[self.index]

	def eof(self):
		return self.index >= len(self.text)