#生成器表达式
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

#Determine if any .py files exist in a directory
# import os
# 需要一个path路径
# files = os.listdir(path)
# if any(name.endswith('.py') for name in files):
# 	print('There be Python!')
# else:
# 	print('Sorry, no Python.')

#Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

#Data reduction across fields of a data structure
portfolio = [
	{'name': 'GOOG', 'shares': 50},
	{'name': 'YHOO', 'shares': 75},
	{'name': 'AOL', 'shares': 20},
	{'name': 'SCOX', 'shares':65}
]
min_shares = min(a['shares'] for a in portfolio)
print(min_shares)