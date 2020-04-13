from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
#Output Subscriber(addr='jonesy@example.com', joined='2012-10-19')
print(sub.addr)
#Output jonesy@example.com
print(sub.joined)
#Output 2012-10-19