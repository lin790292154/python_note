#write by lcj

name = "my name is kra\ttos ,my years old is {year},l am in {where}"

print(name.capitalize())   #首字母大写
print(name.count("a"))      #计算字母数量
print(name.center(5,"-"))  #-----kratos-----
print(name.endswith(".com"))    #判断是否以.com结尾
print(name.expandtabs(tabsize=98)) #替换tab的长度
print(name.find("a"))
print(name[1:2])    #可以切片
print(name.format(year = 18 , where = "shenzhen"))  #格式化输出
print(name.format_map( {"year":18,"where":"sehnzhen"} ))    #格式化输出：使用字典的方式
print('abcD123'.isalnum())   #判断是否是阿拉伯数字或者大小写英文字母
print('abBBD'.isalpha())    #判断是否英文字母
print('13'.isdecimal())     #判断是否是实数
print('235'.isdigit())      #判断是否是整数
print('+'.join(['1','2','3']))  #1+2+3
print(name.ljust(30,'*'))  #不够30时行右补齐*
print(name.rjust(30,'*'))
print("   kratos\n".strip())    #去除左右两边的空格和换行
print("kratos".replace('t','T'))    #替换字符
print('kratos yang'.split('+'))     #以+号为分隔符，结果为列表
print('kratos yang'.splitlines())     #以换行符号为分隔符，结果为列表





