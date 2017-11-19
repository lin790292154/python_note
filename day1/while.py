# write by kratos

'''
count = 0

while True:
    print("count=",count)
    count = count + 1
'''

age_of_oldboy = 66
count = 0
while count < 3 :
    guess_age = int(input("what is oldboy age ?"))

    if age_of_oldboy == guess_age :
        print("you are right")
        break
    elif age_of_oldboy > guess_age:
        print("To small")
    else:
        print("To big")
    count += 1
else:
    print("you have tried too many time,fuck off")

