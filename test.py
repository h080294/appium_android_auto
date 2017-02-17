# -*- coding: utf-8 -*-
import sys

from common import appiumServer
import os
from common import operateYaml
from common.myserver import closed_web_server
from configs.config import conflict_phone
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append("..")
data = {"init": [], "info": []}

#
# def get_devices():
#     return operateYaml.getYam(PATH("../devices.yaml"))
# ga = get_devices()
# # print(ga)
#
# def test():
#     leng = len(ga["appium"])
#     print(leng)
#
# ab = test()


def get_devices():
    return operateYaml.getYam(PATH("configs/devices.yaml"))


def get_conflict(self):
    self.conflict_phone = conflict_phone
    try:
        data = self.conflict_phone.pop()
        return data
        print(data)
        print(conflict_phone)
    except Exception as e:
        raise Exception("got no more value to be popped")

# get_conflict()
print("原集合数据： " + str(conflict_phone))
data = conflict_phone.pop()
print("data数据: " + str(data))
print("改变后的集合数据: " + str(conflict_phone))
username, password = data
print("username is " + username)
print("password is " + password)
