# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constants import globalConstants as c

class TestInvalidlogin3():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_invalidlogin3(self):
    self.driver.get(c.BASE_URL)
    self.driver.maximize_window()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id=\'user-name\']")))
    self.driver.find_element(By.ID, "user-name").click()
    self.driver.find_element(By.NAME, "user-name").send_keys("locked_out_user")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id=\'password\']")))
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    self.driver.find_element(By.ID, "login-button").click()
    assert self.driver.find_element(By.XPATH, "//div[@id=\'login_button_container\']/div/form/div[3]/h3").text == "Epic sadface: Sorry, this user has been locked out."
    self.driver.close()
  
