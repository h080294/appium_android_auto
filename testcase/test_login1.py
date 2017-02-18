# -*- coding: utf-8 -*-
from time import sleep
from runnerBase import TestInterfaceCase


class test_login1(TestInterfaceCase):
    def setUp(self):
        super(test_login1, self).setUp()

    def tearDown(self):
        self.driver.close_app()

    def test_001(self):
        self.driver.find_element_by_id('com.nice.main:id/register').click()
        sleep(2)
