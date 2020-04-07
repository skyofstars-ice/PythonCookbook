#当对象是不可哈希的序列时，想要在其中去除重复项
#这里的key的作用是指定一个函数用来将序列中的元素转换为可哈希的类型，这么做的目的是为了检测重复项
def dedupe(items, key=None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)

a = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2},{'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))