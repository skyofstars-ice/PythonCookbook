#另一个值得一提的筛选工具是 itertools.compress()
#它接受一个可迭代对象以及一个布尔选择器序列作为输入。
#输出时，它会给所有在相应的布尔选择器中为True的可迭代对象元素。
#如果想对一个序列的筛选结果施加到另一个相关的序列上，这就会非常有用。
addresses = [
	'5412 N CLARK',
	'5148 N CLARK',
	'5800 E 58TH',
	'2122 N CLARK',
	'5645 N RAVENSWOOD',
	'1060 W ADDISON',
	'4801 N BROADWAY',
	'1039 WGRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]
#现在我们想构建一个地址列表，其中相应的count值要大于5。
#下面是可以尝试的方法：
from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
#Output[False, False, True, False, False, True, True, False]

more5_list = list(compress(addresses, more5))
print(more5_list)
#Output['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
#这里的关键在于首先创建一个布尔序列，用来表示哪个元素可以满足我们的条件。
#然后compress()函数挑选出满足布尔值为True的相应元素。