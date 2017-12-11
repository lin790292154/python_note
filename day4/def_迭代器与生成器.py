__author__ = "kratos"

"""
 列表生成式：
 a = [i*2 for i in range(10)]   # a = [fun(i) for i in range(10)]

 print(a)
 
生成器：a = （i*2 for i in range(10)）
    特点：
        1.生成器只有在调用时候才会生成响应的数据，只能一次一次生成，不能跨越取值
        2.只记录当前位置，当前数据，只有一个__next__()方法
"""


a = (i*2 for i in range(10))
