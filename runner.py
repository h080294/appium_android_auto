# -*- coding: utf-8 -*-
import sys
import time
import unittest
from common.myserver import closed_web_server
from runnerBase import TestInterfaceCase
from testcase.test_login1 import test_login1
import os
from multiprocessing import Pool
from common import operateYaml
from http.server import HTTPServer
from common import myserver
from multiprocessing import Process
from configs.config import GetVariable
from common import appiumServer

sys.path.append("..")
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

data = {"init": [], "info": []}


def get_devices():
    return operateYaml.getYam(PATH("configs/devices.yaml"))
ga = get_devices()


def runnerCaseWeb():
    pass


def runnerPool():
    devices_Pool = []
    for i in range(0, len(ga["appium"])):
        l_pool = []
        desired_caps = {}
        desired_caps["deviceName"] = ga["appium"][i]["devices"]
        # t["platformVersion"] = phoneBase.get_phone_info(devices=ga["appium"][i]["devices"])["release"]
        desired_caps["platformVersion"] = ga["appium"][i]["platformVersion"]
        desired_caps["platformName"] = ga["appium"][i]["platformName"]
        desired_caps["port"] = ga["appium"][i]["port"]
        l_pool.append(desired_caps)
        devices_Pool.append(l_pool)
    pool = Pool(len(devices_Pool))
    # for i in range(2):
    #     pool.apply_async(sample_request, args=(t[i],)) # 异步
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()


def runnerCaseApp(l_devices):
    suite = unittest.TestSuite()
    suite.addTest(TestInterfaceCase.parametrize(test_login1, l_devices=l_devices))
    unittest.TextTestRunner(verbosity=2).run(suite)


def open_web_server():
    web_server = HTTPServer((GetVariable.HOST, GetVariable.PORT), myserver.myHandler)
    web_server.serve_forever()

if __name__ == '__main__':
    ga = get_devices()
    p = Process(target=open_web_server, args=())
    p.start()
    appium_server = appiumServer.Appium(ga)
    appium_server.start_server()
    while not appium_server.is_runnnig():
        time.sleep(2)
    runnerPool()
    appium_server.stop_server()
    closed_web_server()


