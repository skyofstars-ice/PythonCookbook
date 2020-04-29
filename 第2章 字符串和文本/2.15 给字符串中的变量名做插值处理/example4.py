import sys
s = '{name} has {n} messages'

class safesub(dict):
	def __missing__(self, key):
		return '{' + key + '}'

def sub(text):
	return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}'))  #  Hello Guido
