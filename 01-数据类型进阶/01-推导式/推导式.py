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
2.字典推导式
'''


# res = [f'data{i}' if i%2==0 else f'musen{i}'  for i in range(100)]
# print(res)
i= 12
res = f'偶数：{i}'if i%2==0 else f'奇数{i}'
print(res)