__author__ = "kratos"


def cale(n):
    print(n)
    if n > 1 :
        return cale(n/2)
    print(n)

cale(20)

"""
递归特性：
    1。必须要有一个明确的结束条件
    2.每次递归，问题规模要比上次要小
    3.递归效率不高，而且递归层数过多，会导致栈溢出
"""