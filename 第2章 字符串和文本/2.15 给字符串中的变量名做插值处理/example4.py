import sys

class safesub(dict):
	def __missing__(self, key):
		return '{' + key + '}'

def sub(text):
	return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}'))  #  Hello Guido
print(sub('You have {n} messages'))  #  You have 37 messages
print(sub('Your favorite color is {color}'))  #  Your favorite color is {color}