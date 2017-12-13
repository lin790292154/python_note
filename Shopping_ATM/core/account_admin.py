__author__ = "kratos"


import os
import json
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def add_user():
    with open("{dir}/data/account".format(dir=BASE_DIR),"r") as f1 ,open("{dir}/data/account_new".format(dir=BASE_DIR),"w") as f2:
        credit_card = json.load(f1)
        name = {}
        user = input("please input name for new account:")
        name["name"] = user
        id = input("please input id for new account:")
        passwd = input("please input passwd for new account:")
        name["passwd"] = passwd
        credit = input("please input credit for new account:")
        name["credit"] = credit
        name["balance"] = credit
        name["status"] = "0"
        credit_card[id] = name
        json.dump(credit_card,f2,ensure_ascii=False, indent=4)
        with open("{dir}/log/{id}.log".format(dir=BASE_DIR,id=id),"w") as f3:
            f3.write("{}")
        os.remove("{dir}/data/account".format(dir=BASE_DIR))
        os.rename("{dir}/data/account_new".format(dir=BASE_DIR),"{dir}/data/account".format(dir=BASE_DIR))


def balance_change():
    with open("{dir}/data/account".format(dir=BASE_DIR),"r") as f1 , open("{dir}/data/account_new".format(dir=BASE_DIR),"w") as f2:
        Credit_card = json.load(f1)
        while True:
            id  = input("pleases input want change balance's id : ")
            if id in Credit_card:
                balance = input("please input want change balance to %s : " % Credit_card[id]["name"] )
                Credit_card[id]["balance"] = balance
                json.dump(Credit_card,f2,ensure_ascii=False, indent=4)
                print(Credit_card)
                os.remove("{dir}/data/account".format(dir=BASE_DIR))
                os.rename("{dir}/data/account_new".format(dir=BASE_DIR), "{dir}/data/account".format(dir=BASE_DIR))
                print("Change balance success!!!")
                break
            else:
                print("This id not exist")
                continue

def status_change():
    with open("{dir}/data/account".format(dir=BASE_DIR), "r") as f1, open(
            "{dir}/data/account_new".format(dir=BASE_DIR), "w") as f2:
        Credit_card = json.load(f1)
        while True:
            id = input("pleases input want to lock or unlock id : ")
            if id in Credit_card:
                status = input("please input want change status to {name} , This status is {status} right now : ".format(name=Credit_card[id]["name"],
                                                                                                                         status=Credit_card[id]["status"] )  )
                Credit_card[id]["status"] = status
                json.dump(Credit_card, f2, ensure_ascii=False, indent=4)
                print(Credit_card)
                os.remove("{dir}/data/account".format(dir=BASE_DIR))
                os.rename("{dir}/data/account_new".format(dir=BASE_DIR),
                          "{dir}/data/account".format(dir=BASE_DIR))
                print("Change status success!!!")
                break
            else:
                print("This id not exist")
                continue

#add_user()
#balance_change()
#status_change()