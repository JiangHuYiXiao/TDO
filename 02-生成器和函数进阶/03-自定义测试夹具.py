#!/usr/bin/python
# -*- coding:utf-8 -*-
# @FileName  :03-自定义测试夹具.py
# @Time      :2024/3/26 10:32
# @IDE       :PyCharm
# @Author    :江湖一笑

def  login():
    print('=========前置条件1==========')
    print('=========前置条件2==========')
    print('=========前置条件3==========')
    yield 99999
    print('=========后置条件1==========')
    print('=========后置条件2==========')
    print('=========后置条件3==========')


def test123(login):
    print('=====执行开始========')
    print(login)
    assert 100==100

g1 = login()

res = next(g1)
test123(res)
next(g1)