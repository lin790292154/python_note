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
        name["status"] = 0
        credit_card[id] = name
        json.dump(credit_card,f2,ensure_ascii=False, indent=4)
    os.remove("{dir}/data/account".format(dir=BASE_DIR))
    os.rename("{dir}/data/account_new".format(dir=BASE_DIR),"{dir}/data/account".format(dir=BASE_DIR))



add_user()