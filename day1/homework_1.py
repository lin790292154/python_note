# write by kratos
'''
作业二：编写登陆接口
    输入用户名密码，有一个文件存储用户名密码文件
    认证成功后显示欢迎信息
    输错三次后锁定，下次在使用这个用户名登陆的时候，显示已锁定，使用py文件处理的知识（考虑用list？记录在硬盘里，）
'''

i = 0

while i < 3 :
    user = {}
    _username = "kratos"
    _password = "abc123"
    username = input("please input your username:")
    password = input("please input your passwd:")
    user[username] = password
    if _username == username :
        if _password == password :
            print("Welcom to %s! logging..",username)
        else:
            print("Password unexpect!")
            i+=1

