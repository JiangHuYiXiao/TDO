'''
需求：
使用字典推导式将下面字符串格式的数据，改成字典类型的数据
    cook_str='BIDUPSID=D0727533D7147B7;PSTM=1530348042; BAIDUID=B1005C9BC2EB28; sugstore=0;__cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_lsm=2;BDORZ=B490B5EBF6F3CD402'

转换后的格式
    res = {"BIDUPSID":"D0727533D7147B7","PSTM":"1530348042"....}

'''
cook_str='BIDUPSID=D0727533D7147B7;PSTM=1530348042; BAIDUID=B1005C9BC2EB28; sugstore=0;__cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_lsm=2;BDORZ=B490B5EBF6F3CD402'
# 常规方案：
dic1 = {}
for i in cook_str.split(';'):
    dic1[i.split('=')[0].strip()] =i.split('=')[1].strip()
print(dic1)


# 推导式方案：
res = {i.split('=')[0].strip():i.split('=')[1].strip() for i in cook_str.split(';')}
print(res)

