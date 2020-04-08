rows = [
	{'fname': 'Brain', 'lname': 'Jones', 'uid': 1003},
	{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
	{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
	{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
	]	

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)
#Output rows_by_fname
#[{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, 
#{'fname': 'Brain', 'lname': 'Jones', 'uid': 1003}, 
#{'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
#{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]
#Output rows_by_uid
#[{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, 
#{'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
#{'fname': 'Brain', 'lname': 'Jones', 'uid': 1003}, 
#{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]
