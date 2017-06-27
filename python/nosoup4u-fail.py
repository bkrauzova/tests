#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import sys

class LoginNosoup4u(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get("https://10.130.53.124")
        self.base_url = "https://10.130.53.124" # val-rc7k
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_nosoup4u(self):
        driver = self.driver
        # login with nosoup4u!
        driver.get(self.base_url + "/")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "login-button-connexion"): 
                    break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("login-input-username").clear()
        driver.find_element_by_id("login-input-username").send_keys("admin")
        driver.find_element_by_id("login-input-password").clear()
        driver.find_element_by_id("login-input-password").send_keys("nosoup4u!")
        driver.find_element_by_id("login-button-connexion").click()        

        for i in range(1):
            try:
                if self.is_element_present(By.ID, "uptime-percent"): 
#                if self.is_element_present(By.ID, "datacenters-datacenter-datacenter-1"): 
                    break
                else:
                    print "not found uptime"
            except: pass
            time.sleep(1)
        else: 
            self.fail("time out")


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main(exit=True)


