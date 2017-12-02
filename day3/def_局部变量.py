__author__ = "kratos"

name = "kratos"     #全局变量

def change_name(name):
    print("before name ",name)
    name = "lincj"  #函数中的变量的作用域只作用于函数中，称为局部变量.（复杂数据类型可以更改，比如集合字典列表）
    print("after name ",name)

print(name)

#在函数里修改全局变量
name_1 = "kratos"

def change_name_1(name):
    global name_1
    print("before name ",name)
    name = "lincj"  #函数中的变量的作用域只作用于函数中，称为局部变量
    print("after name ",name)

print(name)