__author__ = "kratos"

def demo_1(a,b):
    print(a)
    print(b)

demo_1("hello","world")  #位置参数：与形参一一对应
demo_1(b = "hello",a = "world")   #关键字调用：位置无需固定


#设置默认参数,特点：调用函数的时候，默认参数非必须传递
def demo_2(x,y=2):
    print(x)
    print(y)

demo_2(3)


#参数不固定的写法1: *args接受N个位置参数，转换成元组
def demo_3(*args):
    print(args)

demo_3(1,3,45,54)

def demo_4(x,*args):
    print(x)
    print(args)

#参数不固定写法2: **kwargs接受N个关键字参数，转化成字典的方式
def demo_5(x,**kwargs):
    print(x)
    print(kwargs)

demo_5(235,fadkg=35,fakdgna='gdfa')