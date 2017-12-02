__author__ = "kratos"

import time

def logger():
    time_module = '%Y-%m-%d  %X'
    time_log = time.strftime(time_module)
    with open("def_text",'a+') as f :
        f.write("This moment is %s \n" %time_log)

def Demo_1():
    print("this demo_1!")
    logger()

def Demo_2():
    print("this demo_2")
    logger()

def Demo_3():
    print("this demo_3")
    logger()

Demo_1()
Demo_2()
Demo_3()





