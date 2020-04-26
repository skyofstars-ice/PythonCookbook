text = 'Hello World'
a = format(text, '>20')
print(a)  #  '         Hello World'

b = format(text, '<20')
print(b)  #  'Hello World         '

c = format(text, '^20')
print(c)  #  '    Hello World     '

d = format(text, '=>20s')
print(d)  #'=========Hello World'

e = format(text, '*^20s')
print(e)  #'****Hello World*****'