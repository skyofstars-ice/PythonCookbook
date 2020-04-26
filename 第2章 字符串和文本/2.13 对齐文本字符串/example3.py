text = 'Hello World'
a = format(text,'>20')
print(a)  #  '         Hello World'

b = format(text,'<20')
print(b)  #  'Hello World         '

c = format(text,'^20')
print(c)  #  '    Hello World     '