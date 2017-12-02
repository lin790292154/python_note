__author__ = "kratos"


def test():
    print("返回值数=0，函数会返回none")

def test_2():
    print("返回值数量=1，函数会返回object！（即返回值本身）")
    return 0

def test_3():
    print("返回值数量>1,函数会返回一个元组tuple！")
    return 1,10,0,"hello,world!",{"name":"xiaohu"},["nginx","tomcat","redis"]

