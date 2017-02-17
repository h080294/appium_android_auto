# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def appium_testcase(l_devices):
    desired_caps = {}
    desired_caps['platformName'] = l_devices["platformName"]
    desired_caps['platformVersion'] = l_devices["platformVersion"]
    desired_caps['deviceName'] = l_devices["deviceName"]
    desired_caps['appPackage'] = "com.nice.main"
    desired_caps['appActivity'] = "com.nice.main.activities.MainActivity_"
    desired_caps['udid'] = l_devices["deviceName"]
    desired_caps['app'] = PATH('configs/nice_main_4.5.0.apk')
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    desired_caps["noRest"] = "True"
    remote = "http://127.0.0.1:" + str(l_devices["port"]) + "/wd/hub"
    driver = webdriver.Remote(remote, desired_caps)
    return driver


class TestInterfaceCase(unittest.TestCase):
    def __init__(self, methodName='runTest', l_devices=None):
        super(TestInterfaceCase, self).__init__(methodName)
        self.l_devices = l_devices


    @staticmethod
    def setUpClass():
        # global driver
        # ga = get_evices()
        # common.SELENIUM_APPIUM = ga.selenium_appium
        # if common.SELENIUM_APPIUM == common.APPIUM: # appium入口
        #     if ga.platformName == common.ANDROID and common.FLAG:
        #         appium_testcase(ga)
        pass

    def setUp(self):
        self.driver = appium_testcase(self.l_devices)

    def tearDown(self):
        # self.driver.close_app()
        # self.driver.quit()
        pass

    @staticmethod
    def tearDownClass():
        # driver.close_app()
        # driver.quit()
        print('tearDownClass')

    @staticmethod
    def parametrize(testcase_klass, l_devices=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, l_devices=l_devices[0]))
        return suite
