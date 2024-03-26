#!/usr/bin/python
# -*- coding:utf-8 -*-
# @FileName  :04-生成器和迭代器的区别.py
# @Time      :2024/3/26 10:33
# @IDE       :PyCharm
# @Author    :江湖一笑

'''
1.生成器是继承与迭代器，迭代器有的方法生成器都有next()取值

2.生成器和迭代器的区别：
    生成器有close()方法
    生成器有send()方法，send方法必须传递一个参数，传递的参数会被上一次yield暂停处的变量接收，必须在生成器使用了一次next之后调用
    生成器有throw()方法  在生成器内部抛出一个异常，在上一次yield暂停的位置抛出异常
'''

def gen_function():
    print('=========前置条件1==========')
    print('=========前置条件2==========')
    print('=========前置条件3==========')
    V1 = yield 99999
    print("V1:",V1)
    V2 = yield 88888
    print("V2:",V2)
    V3 = yield 11111
    print("V3:",V3)
    print('=========后置条件1==========')
    print('=========后置条件2==========')
    print('=========后置条件3==========')


gen1 = gen_function()   # <generator object gen_function at 0x0000017702350A20>
print(next(gen1))       # next()取值 99999
# gen1.send('jianghu')
# close() 关闭生成器后再取值则会提示生成器停止迭代

# print(next(gen1))
# gen1.send('123456')
# gen1.close()
# next(gen1)             # StopIteration

# send() send方法必须传递一个参数，传递的参数会被上一次yield暂停处的变量接收
# gen1.send('999999')


gen1.throw(TypeError)
