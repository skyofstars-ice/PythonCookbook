#序列中的值是可哈希的，就可以通过使用集合和生成器解决
def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]

print(list(dedupe(a)))