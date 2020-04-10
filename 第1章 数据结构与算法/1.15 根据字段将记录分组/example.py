rows = [
	{'address': '5412 N CLARK','date': '07/01/2012'},
	{'address': '5418 N CLARK','date': '07/04/2012'},
	{'address': '5800 E 58TH','date': '07/02/2012'},
	{'address': '2122 N CLARK','date': '07/03/2012'},
	{'address': '5645 N RAVENSWOOD','date': '07/02/2012'},
	{'address': '1060 W ADDISON','date': '07/02/2012'},
	{'address': '4801 N BROADWAY','date': '07/01/2012'},
	{'address': '1039 W GRANVILE','date': '07/04/2012'},
]
#现在假设根据日期以分组的方式迭代数据。
#要做到这些，首先以目标字段（在这个例子中是date）来对序列排序，然后再使用itertools.groupby()
from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
	print(date)
	for i in items:
		print(' ', i)

#Output
# 07/01/2012
#   {'address': '5412 N CLARK', 'date': '07/01/2012'}
#   {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
# 07/02/2012
#   {'address': '5800 E 58TH', 'date': '07/02/2012'}
#   {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}
#   {'address': '1060 W ADDISON', 'date': '07/02/2012'}
# 07/03/2012
#   {'address': '2122 N CLARK', 'date': '07/03/2012'}
# 07/04/2012
#   {'address': '5418 N CLARK', 'date': '07/04/2012'}
#   {'address': '1039 W GRANVILE', 'date': '07/04/2012'}