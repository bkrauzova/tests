# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LoginFirst(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://bara.roz.lab.etn.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_first(self):
        driver = self.driver
        # Login with admin -> change psw -> acc. licence -> def. network ->create empty DC -> logout
        driver.get(self.base_url + "/")
        assert (false)
