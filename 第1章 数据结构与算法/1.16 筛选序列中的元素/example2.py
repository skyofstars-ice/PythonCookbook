#关于筛选数据，有一种情况是用新值替换掉不满足标准的值，而不是丢弃它们。
#例如，除了要找到正整数以外，我们也许还希望在指定的范围内将不满足要求的值替换掉。
#通常，这可以通过筛选条件移到一个条件表达式中来轻松实现。
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
#Output[1, 4, 0, 10, 0, 2, 3, 0]

clip_pos = [x if x < 0 else 0 for x in mylist]
print(clip_pos)
#Output[0, 0, -5, 0, -7, 0, 0, -1]