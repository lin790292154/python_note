
#  write by kratos
#

#name = raw_input("What is your name?") #only on python 2.x


name = input("Your name:")
job = input("Your job:")
salary = input("Your salary:")


#多行输出字符串，结合变量表达方式1：字符串拼接,该方法会开辟多块内存，正常不使用这种方法
info = '''
--------info of you-------
name:''' + name + '''
job: '''+ job +'''
salary'''+ salary


print(info)

#多行输出字符串，结合变量表达方式2：格式输出
info_1 = '''
-------infoo of you------
Name:%s
job:%s
salay:%s
''' %(name,job,salary)

print(info_1)

#多行输出字符串，结合变量表达方式2：多种格式化输出，并强制转换数据类型
name = input("Your name:")
job = input("Your job:")
salary = int( input("Your salary:") )  #integer整型
print(type(salary))  #type()函数：打印变量的类型

info_2 = '''
-------infoo of you------
Name:%s
job:%s
salay:%d
''' %(name,job,salary)

print(info_2)

#多行输出字符串，结合变量表达方式3:在特定场景下使用个性化拼接，只能使用下面的方法
info_3 = '''
-------infoo of you------
Name:{_name}
job:{_job}
salay:{_salary}
''' .format(_name=name,
            _job=job,
            _salary=salary
            )

print(info_3)

#多行输出字符串，结合变量表达方式4
info_3 = '''
-------infoo of you------
Name:{0}
job:{1}
salay:{2}
''' .format(name,job,salary)

print(info_3)






