#内建的sorted()函数可接受一个用来传递可调用对象(callable)的参数key，
#而该可调用对象会返回待排序对象的某些值，sorted则利用这些值来比较对象。
#例如，如果应用中有一系列的User对象实例，而我们想通过user_id属性来对它们排序，
#则可以提供一个可调用对象将User实例作为输入然后返回user_id。
#示例如下：
class User:
	def __init__(self, user_id):
		self.user_id = user_id
	def __repr__(self):
		return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]

print(sorted(users, key = lambda u: u.user_id))

#from operator import attrgetter
#print(sorted(users, key = attrgetter('user_id')))