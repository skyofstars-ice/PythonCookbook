s = '{name} has {n} messages'
class Info:
	def __init__(self, name, n):
		self.name = name
		self.n = n
a = Info('Guido', 37)
b = s.format_map(vars(a))
print(b)  #  Guido has 37 messages