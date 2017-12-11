__author__ =  "kratos"

import  time

'''
装饰器的定义：
    本质是函数，（装饰其他函数）就是为其他函数添加附加功能
原则：
    1。函数写完上线之后，原则上不能修改被装饰的函数源代码。
    2。不能修改被装饰的函数的调用方式。
实现装饰器知识储备：
    1.函数即“变量”：在内存使用方式上是相同的
        a：把一个函数名当做实参传给另外一个函数 
        b:返回值中包含函数名
    
    2.高阶函数
        a：把一个函数名当做实参传给另外一个函数（在不修改被装饰函数源代码的情况下添加功能）
        b：返回值中包含函数名（  不修改函数的调用方式）
    3.嵌套函数
        
'''

def timmer(func):
    def add_timmer_tomcat() :
        start_time = time.time()
        func()
        stop_time =  time.time()
        print("This is add_time %f"  %(stop_time - start_time))
    return add_timmer_tomcat


@timmer
def tomcat():
    print("This is toxiangtou mcat")
    time.sleep(3)

tomcat()