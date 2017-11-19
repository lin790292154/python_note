# write by kratos



age_of_oldboy = 66
for i in range(3):
    guess_age = int(input("what is oldboy age ?"))

    if age_of_oldboy == guess_age :
        print("you are right")
        break
    elif age_of_oldboy > guess_age:
        print("To small")
    else:
        print("To big")
else:   #代表上面的代码如果正常走玩没有break，就会执行else的代码。
    print("you have tried too many time,fuck off")

