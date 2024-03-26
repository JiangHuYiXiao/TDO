# 生成器定义方式


# 1.生成器推导式
ge = (i for i in range(10))
print(ge)     # <generator object <genexpr> at 0x000002A0BD6A9A20>
# 2.生成器函数

def generator_func():
    print('=====yield前置执行===1===')
    print('=====yield前置执行===2===')
    print('=====yield前置执行===3===')
    yield '6666666'
    yield '1111111'
    print('=====yield之后执行===1===')
    print('=====yield之后执行===2===')
    print('=====yield之后执行===3===')

ge1 = generator_func()
print(ge1)   # <generator object generator_func at 0x00000244FFDD9A98>
print(next(ge1))    # 6666666
print(next(ge1))    # 1111111
print(next(ge1))    # StopIteration
# try:
# #     print(next(ge1))
# # except StopIteration as e:
# #     print(e)