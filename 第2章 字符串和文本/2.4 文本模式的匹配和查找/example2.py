text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
if re.match(r'\d+/\d+/\d+', text1):
	print('text1 is yes')
else:
	print('text2 is no')

if re.match(r'\d+/\d+/\d+', text2):
	print('text2 is yes')
else:
	print('text2 is no')