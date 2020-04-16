filename = 'spam.txt'
a = filename.endswith('txt')
print(a)
b = filename.startswith('file:')
print(b)
url = 'http://www.python.org'
c = url.startswith('http:')
print(c)