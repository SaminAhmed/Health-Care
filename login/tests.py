import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR,'/gecko')
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AccountTestCase(LiveServerTestCase):
    def test_login(self):
     driver = webdriver.Chrome()
     driver.get('http://127.0.0.1:8000/login')
     username = driver.find_element_by_id('email')
     password = driver.find_element_by_id('password')
     submit = driver.find_element_by_id('sub')
     #username.send_keys('superusername')
     #password.send_keys('superuserpassword')

     username.send_keys('sakib@gmail.com')
     password.send_keys('sakib')
     submit.send_keys(Keys.RETURN)

     #assert 'Sakib' in driver.page_source


