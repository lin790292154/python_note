#write by lincj
# -*- coding:utf-8 -*-

#编码详解url:www.cnblogs.com/luotianshuai/articles/5735051.html

# python3中所有数据类型都是unicode格式编码的
# python3中只要encode之后，不光转换成编码而且都变成了byte格式。
# decode():所有的decode都是解码成Unicode，参数为当前的字符的编码
# encode():不加参数转成默认编码，加上参数转成想要的编码
# utf-8要转码成gbk，需要先decode，再encode成gbk

s = "你好"

s1 = s.decode("utf-8")
print(s1)