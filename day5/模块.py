'''
1.定义：
    模块：用来从逻辑上组织python代码（代码，函数，类，逻辑：实现一个功能）模块本质就是.py结尾的Python文件.(test.py文件对应的模块名就是test)
    包：用来从逻辑上组织模块的，本质就一个目录（必须带有一个__init__.py文件）

2.导入方法
    import module_name
    import module_name,module1_name
    from module_name import *   ##导入模块下所有的方法，
    from module_name import m1,m2,m3
    from modele_name import logger as logger_alex   ##起别名

3.import本质（路径搜索和搜索路径）
    导入模块的本质：就是把python文件解释一遍：
        情况一：
            import module_name :
            module_name = all_code(把所有代码解释一遍，然后赋值，所以这种方式需要用module_name引用执行)

        情况二：
            from module_name import name
            name = "kratos"    #相当于在当前的文件，打开这个module文件导入，执行这行代码，所以这种方式不需要用module_name引用执行

    导入包的本质：就是执行该包下的__init__.py文件

    sys.path 是一个列表

4.导入优化
5.模块的分类



'''