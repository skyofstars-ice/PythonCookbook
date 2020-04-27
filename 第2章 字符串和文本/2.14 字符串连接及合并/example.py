parts = ['Is','Chicago','Not','Chicago?']

a = ' '.join(parts)
print(a)  #  Is Chicago Not Chicago?

b = ','.join(parts)
print(b)  #  Is,Chicago,Not,Chicago?

c = ''.join(parts)
print(c)  #  IsChicagoNotChicago?