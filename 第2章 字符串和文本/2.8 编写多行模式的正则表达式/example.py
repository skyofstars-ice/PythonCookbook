import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/*this is a comment*/'
text2 = '''/*this is a
				multiline comment*/
	
'''

a = comment.findall(text1)
print(a)
b = comment.findall(text2)
print(b)

