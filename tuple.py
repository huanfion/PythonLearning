#元组 不可改变的列表
#遍历元组
change_tuple=(1,2,3,4)
for x in change_tuple:
    print(x)
change_tuple=(11,22,33,44)
print("元组不可改变，赋值操作结果：")
for x in change_tuple:
    print(x)
#元组元素修改报错：TypeError: 'tuple' object does not support item assignment
#change_tuple[0]=111
print(change_tuple[0])


