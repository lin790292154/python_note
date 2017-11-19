# write by kratos
# 使用if语句
import getpass


_username = "kratos"
_password = "123"

username = input("usernaem:")
password = input("password:")

print(username,password)

#强制缩进的好处：1.结构清晰，又美观。2.减少代码量。
if _username == username and _password == password:
    print("Welcome user {name} loging ...".format(name=username))
else:
    print("Invalid usernaem or password!")

#-----------------------------------------------------------------

age_of_oldboy = 66

guess_age = int(input("what is oldboy age ?"))

if age_of_oldboy == guess_age :
    print("you are right")
elif age_of_oldboy > guess_age:
    print("To small")
else:
    print("To big")

