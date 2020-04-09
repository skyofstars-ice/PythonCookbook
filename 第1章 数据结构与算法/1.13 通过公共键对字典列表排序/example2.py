rows = [
	{'fname': 'Brain', 'lname': 'Jones', 'uid': 1003},
	{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
	{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
	{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
	]	

from operator import itemgetter
#itemgetter()函数还可以接受多个键
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))

print(rows_by_lfname)

#Output rows_by_lfname
#[{'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
#{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, 
#{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
#{'fname': 'Brain', 'lname': 'Jones', 'uid': 1003}]
