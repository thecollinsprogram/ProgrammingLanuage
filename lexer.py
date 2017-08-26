from token import *

NUMBERS = []
for i in range(0, 10):
	NUMBERS.append(str(i))

a_z = []
for i in range(ord("a"), ord("z") + 1):
	a_z.append(chr(i))

def lex(code, symbols, keywords):
	i = 0
	tokens = []
	while i < len(code):
		token, increment = findToken(code, i, symbols, keywords)
		if token:
			tokens.append(token)
		i += increment
			
	return tokens
	
def findToken(code, i, symbols, keywords):
	token = findNumber(code, i)
	if token:
		return token
	token = findSymbol(code, i, symbols)
	if token:
		return token
	token = findSymbol(code, i, keywords)
	if token:
		return token
	token = findString(code, i)
	if token:
		return token
	token = findIdentifier(code, i)
	if token:
		return token
	
	return (False, 1)

def findNumber(code, i):
	length = 0
	iden = ""
	flt = False
	
	if code[i + length] == "-":
		iden += code[i]
		length += 1
		
	if code[i + length] in NUMBERS:
		while i + length < len(code) and (code[i + length] in NUMBERS or code[i + length] == "."):
			iden += code[i + length]
			if code[i + length] == ".":
				flt = True
			length += 1
		
		if flt:
			return (Token("flt", iden), length)
		else:
			return (Token("int", iden), length)
			
	return False
	
def findSymbol(code, i, symbols):
	for sym in symbols:
		length = 0
		good = True
		while length < len(sym):
			if i + length >= len(code) or code[i + length] != sym[length]:
				good = False
				break
			length += 1
		if good:
			return (Token(sym, ""), length)
			
	return False
	
def findString(code, i):
	if code[i] == "\"":
		string = ""
		length = 1
		while code[i + length] != "\"":
			string += code[i + length]
			length += 1
			
		return (Token("str", string), length)
		
	return False
	
def findIdentifier(code, i):
	if code[i].lower() in a_z or code[i] == "_":
		length = 1
		iden = code[i]
		while i + length < len(code) and (code[i + length].lower() in a_z or code[i + length] in NUMBERS or code[i + length] == "_"):
			iden += code[i + length]
			length += 1
			
		return (Token("id", iden), length)
			
	return False