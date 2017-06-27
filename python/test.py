#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time, re

class LoginFirst(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get("https://192.168.122.173")
        self.base_url = "https://validation-rc7.roz.lab.etn.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login (self):
        driver = self.driver
        # Login with admin -> change psw -> acc. licence -> def. network ->create empty DC -> logout
        driver.get(self.base_url + "/")

        elem = driver.find_element_by_id ("login-input-username")
        elem.clear()
        elem.send_keys("admin")
        elem = driver.find_element_by_id ("login-input-password")
        elem.clear()
        elem.send_keys("nosoup4u!")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()

