# -*- coding: utf-8 -*-
import os


def stopHTTP():
    command = "lsof -i:8088"
    r = os.popen(command)
    info = r.readlines()
    for line in info:  # 按行遍历
        eachline = line.split()
        server_pid = eachline[1]
        os.popen("kill " + str(server_pid))


def stopAppium():
    r = os.popen("ps -ef | grep appium")
    info = r.readlines()
    for line in info:  # 按行遍历
        eachline = line.split()
        appium_pid = eachline[1]
        action = os.popen("kill " + appium_pid)
        print("kill" + appium_pid)

stopHTTP()
stopAppium()
