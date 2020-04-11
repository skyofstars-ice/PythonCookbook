my_list = [1, 4, -5, 10, -7, 2, 3, -1]

for n in my_list:
	if n > 0:
		print(n)

for i in my_list:
	if i < 0:
		print(i)

#使用列表推导式的一个潜在缺点是如果原始输入非常大的话，这么做可能会产生一个庞大的结果
#如果考虑这种结果，那么可以用生成器表达式通过迭代的方式产生筛选的结果
#例如
pos = (n for n in my_list if n > 0)
for x in pos:
	print(x)