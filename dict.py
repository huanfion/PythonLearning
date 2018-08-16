alien_0 = {'color': 'green', 'points': 5}
print(alien_0["color"])
print(alien_0["points"])
#添加字典 字典是无序的
alien_0["y_position"]=25
print(alien_0)
#删除
del alien_0["y_position"]
print(alien_0)
#遍历字典，默认是遍历key
for key in alien_0.keys():
    print("key:",key)
for value in alien_0.values():
    print("value:",value)
for k,v in alien_0.items():
    print("key:",k,"value:",v)

def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name + "!"
        print(msg)

usernames = ['Hannah', 'Ty', 'Margot']
greet_users(usernames)

