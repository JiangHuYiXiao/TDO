'''
三者之间的迭代关系：
class Iterable:
    pass
class Iterator(Iterable):
    pass

class Generator(Iterator):
    pass

1.可迭代对象（Iterable）：继承object类
    # 1.1能够使用for循环进行遍历的都是可迭代对象

    # 1.2所有序列类型：list、tuple、str、range

    # 1.3非序列类型：dict、set、文件对象:f=open(xx)
        from collections.abc import Iterable,Iterator,Generator
        f = open(r'D:\TD\01-数据类型进阶\01-推导式\综合小练习.py',mode='r',encoding='utf-8')
        print(isinstance(f,Iterable))
    # 1.4实现了__iter__()魔术方法的任意对象（迭代协议）
        class Myclass:
        # 对象迭代时调用的方法
        def __iter__(self):
            return iter([1,2,3])   # 必须return， iter（xxx）返回值是一个迭代器

        m = Myclass()
        for i in m:
            print(i)
    # 1.5实现了序列语义的__getitem__()魔术方法的任意对象
        li = [1,2,3]
        res = li[0]  # 列表中的索引取值，实际内部执行的是__getitem__(0)  x.__getitem__(y) <==> x[y]
        list()

        class Myclass:
            li= [1,2,3]
            def __getitem__(self,item):   # 对象迭代时使用
                return self.li[item]
        m = Myclass()
        for i in m:
            print(i)
******两个都有先调用__iter__(),再执行__getitem__(),两个都没有则不可迭代*****

2.迭代协议：对象拥有了__iter__()魔术方法的，那么这个对象就实现了迭代协议
    class Myclass:
        # 对象迭代时调用的方法
        def __iter__(self):
            return iter([1,2,3])   # 必须return iter（xxx）返回值是一个迭代器

    m = Myclass()
    for i in m:
        print(i)


# 2.迭代器（Iterator）：继承可迭代对象类
实现了迭代器协议的对象，被称为迭代器
2.1 迭代器协议：
    迭代器协议由__iter__()和__next__()共同组成，实现了这两个方法的对象就实现了迭代器协议。
2.2 可迭代对象都可以使用iter()方法传入一个可迭代对象后，生成一个迭代器
    list()
    li = [1,2,3,4,5]
    res = iter(li) # ===>li.__iter__()
    print(res)   # <list_iterator object at 0x000001D5D4C8F940>
    print(next(res))
    print(next(res))
2.3 迭代器都可以使用next()方法进行取值，每次只能迭代一个数据，全部数据迭代完成之后，
    迭代器会关闭，再使用next()取值则会抛出异常StopIteration



# 3.生成器（Generator）：继承迭代器类，就是迭代器的应用

    在大数据存储时生成器占用的内存比迭代器小的多
'''


