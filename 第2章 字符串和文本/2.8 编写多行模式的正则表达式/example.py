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

comment_text = re.compile(r'/\*((?:.|\n)*?)\*/')
c = comment_text.findall(text2)
print(c)

