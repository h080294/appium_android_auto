# -*- coding: utf-8 -*-
import os
from time import sleep
from runnerBase import TestInterfaceCase
from configs.config import conflict_phone


class test_login1(TestInterfaceCase):
    def setUp(self):
        super(test_login1, self).setUp()

    def tearDown(self):
        self.driver.close_app()

    def test_longinToFeed(self):
        sleep(10)
        elem = self.driver.find_element_by_id('com.nice.main:id/login')
        elem.click()
        phoneNumber, password = self.get_conflict()
        self.driver.find_element_by_id('com.nice.main:id/phone_number').clear()
        self.driver.find_element_by_id('com.nice.main:id/phone_number').send_keys(phoneNumber)
        sleep(2)
        self.driver.find_element_by_id('com.nice.main:id/password').send_keys(password)
        sleep(2)
        self.driver.find_element_by_id('com.nice.main:id/login').click()
        sleep(5)

    def get_conflict(self):
        self.conflict_phone = conflict_phone
        try:
            data = self.conflict_phone.pop()
            print("取到的data数据: " + str(data))
            return data
        except Exception as e:
            raise Exception("got no more value to be popped")
