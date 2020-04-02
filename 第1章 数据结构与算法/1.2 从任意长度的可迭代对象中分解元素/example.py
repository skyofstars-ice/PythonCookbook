# *式的语法在迭代一个变长的元组序列时尤其有用。
# 例如下面，假设有一个带标记的元组序列：

records = [
	('foo', 1, 2),
	('bar', 'hello'),
	('foo', 3, 4),
]

def do_foo(x, y):
	print('foo', x, y)

def do_bar(s):
	print('bar', s)

for tag, *args in records:
	if tag == 'foo':
		do_foo(*args)
	elif tag == 'bar':
		do_bar(*args)