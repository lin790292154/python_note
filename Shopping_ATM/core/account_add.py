__author__ = "kratos"


import os
import json
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def add_user():
    with open("{dir}/data/account".format(dir=BASE_DIR),"a") as f1 :
        name = input("please input name for new account:")
        name = {}
        id = input("please input id for new account:")
        name["id"] = id
        passwd = input("please input passwd for new account:")
        name["passwd"] = passwd
        credit = input("please input credit for new account:")
        name["credit"] = credit
        name["balance"] = credit
        name["status"] = 0
        json.dump(name,f1)


add_user()