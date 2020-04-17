text = 'yeah, but no , but yeah, but no, but yeah'

a = (text == 'yeah')
print(a)
b = text.startswith('yeah')
print(b)
c = text.endswith('yeah')
print(c)
d = text.find('no')
print(d)