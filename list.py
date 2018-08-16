bicycles = ['demo', 'chen', 'sen', 'lin']
print(bicycles)

print("取第0个索引:",bicycles[0])
print("取第一个索引:",bicycles[1])
print("取第最后一个索引的值:" + bicycles[-1])

#拼接列表 join
print(",".join(bicycles))
#添加
bicycles.append("goods")
print(bicycles)
#IndexError: list assignment index out of range
#bicycles[5]="news"
#print(bicycles)
#添加元素到固定位置
bicycles.insert(1,"news")
print(bicycles)

#删除元素
#1.del
del bicycles[0]
print(bicycles)

#2.pop 弹出删除最后一个
bicycles.pop()
print(bicycles)

#3.remove 按值删除
bicycles.remove('lin')
print(bicycles)
# sorted sort reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
#根据字母永久排序
cars.sort(reverse=True)
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)


#遍历list
for car in cars:
    print(car)

#创建数值列表 range 包左不包右
print (list(range(1,11)))
print(list(range(1,11,2)))

squares=[value**2 for value in range(1,11)]
print(squares)


#===========================切片===============================
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print("取从索引0开始到第三个结束，最后输出前三个players[0:3]",players[0:3])
print("输出从索引1到4结束，players[1:4]",players[1:4])
print("没有索引就从列表开头开始，到指定的索引值结束players[:4]",players[:4])
print("步数为2players[::2]",players[::2])
#利用步数可以倒序list
print("倒序列表players[::-1]",players[::-1])