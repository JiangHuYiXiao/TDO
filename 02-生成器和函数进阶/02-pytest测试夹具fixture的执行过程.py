#!/usr/bin/python
# -*- coding:utf-8 -*-
# @FileName  :02-pytest测试夹具fixture的执行过程.py
# @Time      :2024/3/26 10:32
# @IDE       :PyCharm
# @Author    :江湖一笑

import pytest

@pytest.fixture     # pytest方式放开，不是pytest则放开
def login():
    print('========登录前置条件1=======')
    print('========登录前置条件2=======')
    print('========登录前置条件3=======')
    yield (666666)
    print('========登录后置条件1========')
    print('========登录后置条件2========')
    print('========登录后置条件3========')

def test_login(login):
    print('===========测试用例执行开始==========')
    print(login)
    assert 100==100

# 使用pytest 命令执行
# D:\TD\02-生成器和函数进阶>pytest -v -s 02-pytest测试夹具fixture的执行过程.py



# 实际执行的代码过程就是这样的
g1 = login()
value = next(g1)
test_login(value)
next(g1)

