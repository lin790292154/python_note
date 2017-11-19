# write by kratos
# 使用密文密码
import getpass


#shell常规方式,实现密文密码比较麻烦
username = input("username:")
password = input("passwd:")

print(username,password)

#python中使用模块简单实现
username = input("usernaem:")
password = getpass.getpass("password:")

print(username,password)

