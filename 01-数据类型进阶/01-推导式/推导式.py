'''
1.列表推导式
    作用：快速往列表中添加数据

    需求1：如何快速生成一个`["data0",'data1',........'data99']`的列表？
        实现方案1：for循环
            li = []
            for i in range(100):
                li.append(f'data{i}')
            print(li)
        实现方案2：列表推导式
    基础版语法：[i for i in xxx]
        [f'data{i}' for i in range(100)]


    需求2：生成一个['data1','data3','data5'......''data99]的列表

    进阶版语法：[i for i in xxx if 条件]
        [f'data{i}' for i in range(100) if i%2==1]


    需求3：生成一个['data0', 'musen1', 'data2', 'musen3'.......'data98','musen99']列表

    高阶版语法：[x if 条件 else y for i in xxx]
        [f'data{i}' if i%2==0 else f'musen{i}'  for i in range(100)]

    高阶版语法等同于：[三目运算符 for i in xxx]

    三目运算符语法： v1 if 条件 else v2   条件成立输出v1,条件不成立输出v2

    扩展：列表推导式同时拥有三目运算符和if条件
        语法：[x if 条件1 else y for i in xxx if 条件2]

2.字典推导式：快速往字典中添加数据
语法：{for key:value in xx}

需求1：有一个列表，li=[a,b,c,d,e,f],请将列表的索引转换为一个字典的key，列表的值转换为字典的value
    常规语法实现:
        方式1：
        li=['a','b','c','d','e','f']
        res1 = enumerate(li)
        res2 = list(res1)
        res4 = dict(res2)
        print(res4)

        方式2：
        dic1 = {}
        for key,value in enumerate(li):
        dic1[key] = value
        print(dic1)


    字典推导式实现:
        res3 = {key:value for key,value in enumerate(li)}
        print(res3)


3.集合推导式:
语法：{i for i in xxx}
    li = ['a','b','c','d','e','f']
    res = {i for i in li}
    print(res)


4.元组推导式(就是生成器表达式)
    res2 = (i for i in li)
    print(res2)  # <generator object <genexpr> at 0x0000018E458B9B88>
'''


# 集合推导式:
# 语法：{i for i in xxx}
li = ['a','b','c','d','e','f']
res = {i for i in li}
print(res)

# 元组推导式(就是生成器表达式)
res2 = (i for i in li)
print(res2)  # <generator object <genexpr> at 0x0000018E458B9B88>
