import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1)) # ['no.']

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2)) # ['no." Phone says "yes.']

#  *操作符是贪心策略，所以匹配过程中是基于找出最长的可能匹配来进行的。
#  要解决这个在text2中错误匹配的问题，只要在模式中的*操作符后加上？修饰符即可
new_str_pat = re.compile(r'\"(.*?)\"')
print(new_str_pat.findall(text2)) # ['no.', 'yes.']