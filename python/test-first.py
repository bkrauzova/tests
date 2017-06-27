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
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "login-button-connexion"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # Password
        driver.find_element_by_id("login-input-username").clear()
        driver.find_element_by_id("login-input-username").send_keys("admin")
        driver.find_element_by_id("login-input-password").clear()
        driver.find_element_by_id("login-input-password").send_keys("admin")
        driver.find_element_by_id("login-button-connexion").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "wizard-passwd-submit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("wizard-input-current").clear()
        driver.find_element_by_id("wizard-input-current").send_keys("admin")
        driver.find_element_by_id("wizard-input-new").clear()
        driver.find_element_by_id("wizard-input-new").send_keys("nosoup4u!")
        driver.find_element_by_id("wizard-input-repeat").clear()
        driver.find_element_by_id("wizard-input-repeat").send_keys("nosoup4u!")
        driver.find_element_by_id("wizard-passwd-submit").click()
        # License
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "wizard-licence-accept"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("wizard-licence-accept").click()
        driver.find_element_by_id("wizard-licence-submit").click()
        # Network setting
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "wizard-network-submit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("wizard-network-submit").click()
        # Create DC
        driver.find_element_by_id("wizard-dc-name").clear()
        driver.find_element_by_id("wizard-dc-name").send_keys("DC-Roztoky")
        driver.find_element_by_id("wizard-dc-max-power").clear()
        driver.find_element_by_id("wizard-dc-max-power").send_keys("15")
        driver.find_element_by_id("wizard-licence-submit").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "wizard-licence-submit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # Add rooms/rows to your new DC
        driver.find_element_by_id("wizard-licence-submit").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "wizard-licence-submit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("wizard-licence-submit").click()
        # Upload csv
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "asset-management-popup-cancel"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("asset-management-popup-cancel").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "navbar-top-home"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
    
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
    unittest.main()
