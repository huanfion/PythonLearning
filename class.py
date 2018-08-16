class Dog():
    # 创建一个小狗的类
    def __init__(self,name,age):
        # 初始化属性name和age
        self.name = name
        self.age = age
    def sit(self):
        # 模拟小狗被命令时蹲下
        print(self.name.title() + " is now sitting !")
    def roll_over(self):
        # 打滚
        print(self.name.title() + " rolled over!")


class Car():
    # Car类
    def __init__(self, name, model, year):
        # 初始化
        self.name = name
        self.model = model
        self.year = year

    def get_descript(self):
        # 返回描述信息
        long_name = str(self.year) + '---' + self.name + '---' + self.model
        return long_name.title()


# 示例化
my_car = Car('audi', 'A4', '2016')
print(my_car.get_descript())

my_dog=Dog('demo',18)
print(my_dog.name)
print(my_dog.age)

f=open("D:\Work\huanfion\python\Learning\dict.py",'r',encoding='utf-8')
print(f.read())