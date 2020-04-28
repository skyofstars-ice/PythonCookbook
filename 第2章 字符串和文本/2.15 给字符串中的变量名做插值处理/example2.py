s = '{name} has {n} messages'
name = 'Guido'
n = '37'
a = s.format_map(vars())
print(a)  #  Guido has 37 messages