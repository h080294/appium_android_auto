# -*- coding: utf-8 -*-
import os
from time import sleep
from multiprocessing import Process
import threading

import requests

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AppiumServer:
    def __init__(self, l_devices):
        self.l_devices = l_devices

    def start_server(self):
        """start the appium server
        :return:
        """
        appium_process_list = []
        for i in range(0, len(self.l_devices["appium"])):
            cmd = self.l_devices["appium"][i]["config"]
            p = Process(target=os.system, args=(cmd,))
            print("开始p.start第" + str(i) + "次")
            print(self.l_devices["appium"][i]["config"])
            appium_process_list.append(p)
            if self.is_runnnig():
                self.stop_server()
        for p in appium_process_list:
            p.start()

    def stop_server(self):
        """stop the appium server
        selenium_appium: appium selenium
        :return:
        """
        r = os.popen("ps -ef | grep appium")
        info = r.readlines()
        for line in info:  # 按行遍历
            eachline = line.split()
            appium_pid = eachline[1]
            os.popen("kill " + appium_pid)
            print("kill appium pid: " + appium_pid)

    def re_start_server(self):
        """reStart the appium server
        """
        self.stop_server()
        self.start_server()

    def is_runnnig(self):
        """Determine whether server is running
        :return:True or False
        """
        response = None
        for i in range(0, len(self.l_devices["appium"])):
            try:
                url = " http://127.0.0.1:" + str(self.l_devices["appium"][i]["port"]) + "/wd/hub"
                result = requests.get(url)
                if result.status_code == 404:
                    return True
                else:
                    return False
            except Exception as e:
                return False
