prices = {
	"ACME": 45.23,
	"AAPL": 612.78,
	"IBM": 205.55,
	"HPQ": 37.20,
	"FB": 10.75
}
#字典推导式
#Make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200}
print(p1)
#Output
#{'AAPL': 612.78, 'IBM': 205.55}

#Make a dictionary of tech stocks
tech_names = {"AAPL", "IBM", "HPQ", "MSFT"}
p2 = { key:value for key, value in prices.items() if key in tech_names}
print(p2)
#Output
#{'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.2}

#大部分可以用字典推导式解决的问题也可以通过创建元组序列然后将它们传给dict()函数来完成
#例如
p3 = dict((key, value) for key, value in prices.items() if value > 200)
print(p3)

#但是字典推导式的方案更加清晰，而且实际运行起来也要快很多
#第二个例子还可以重写为
p4 = { key:prices[key] for key in prices.keys() & tech_names}
print(p4)
#但是计时表明这种方案几乎比字典推导式慢上1.6倍