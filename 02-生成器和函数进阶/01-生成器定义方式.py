#!/usr/bin/python
# -*- coding:utf-8 -*-
# @FileName  :01-生成器定义方式.py
# @Time      :2024/3/26 10:31
# @IDE       :PyCharm
# @Author    :江湖一笑

"""
# 方式1.生成器表达式
ge = (i for i in range(10))
print(ge)   # <generator object <genexpr> at 0x0000025C59660A20>

"""


# 方式2.生成器函数
def gen_function():
    print('======前置条件1=======')
    print('======前置条件2=======')
    print('======前置条件3=======')
    yield(999)
    print('======后置条件1=======')
    print('======后置条件2=======')
    print('======后置条件3=======')


g1 = gen_function()
print(g1)     # <generator object gen_function at 0x0000020CA26A0A20>
res = next(g1)
print(res)    # 999

try:
    next(g1)
except StopIteration as e:
    print(e)


