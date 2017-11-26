__author__ = "kratos"

#linux进度条实现的方法

import sys,time

for i in range(50):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(1)