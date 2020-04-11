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

#有时候筛选的标准没办法简单地表示在列表推导式或者生成器表达式中。
#比如，假设筛选过程涉及异常处理或者其他一些复杂的细节。
#基于此，可以将处理筛选逻辑的代码放到单独的函数中，然后使用内建的filter()函数处理。
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False
ivals = list(filter(is_int, values))
print(ivals)
#Outputs
#['1', '2', '-3', '4', '5']