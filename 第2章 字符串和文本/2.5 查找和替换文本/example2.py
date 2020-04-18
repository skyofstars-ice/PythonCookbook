text = 'Today is 11/27/2012, PyCon starts 3/13/2013'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
#Today is 2012-11-27, PyCon starts 2013-3-13

#sub()的第一个参数是要匹配的模式，第二个参数是要替换上的模式。