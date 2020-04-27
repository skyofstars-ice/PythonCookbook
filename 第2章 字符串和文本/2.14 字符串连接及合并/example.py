parts = ['Is','Chicago','Not','Chicago?']

a = ' '.join(parts)
print(a)  #  Is Chicago Not Chicago?

b = ','.join(parts)
print(b)  #  Is,Chicago,Not,Chicago?

c = ''.join(parts)
print(c)  #  IsChicagoNotChicago?

partone = 'Is Chicago'
parttwo = 'Not Chicago?'

d = '{} {}'.format(partone,parttwo)
print(d)  #  Is Chicago Not Chicago?


# 利用生成器表达式将数据转换为字符串的同时完成连接操作
data = ['ACME', 50, 91.1]
e = ','.join(str(d) for d in data)
print(e)  #  ACME,50,91.1