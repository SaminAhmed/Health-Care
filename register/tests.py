import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR,'/gecko')
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestCase(LiveServerTestCase):
    def test_register(self):
     driver = webdriver.Chrome()
     driver.get('http://127.0.0.1:8000/createaccount')
     uname = driver.find_element_by_id('name')
     username = driver.find_element_by_id('email')
     password = driver.find_element_by_id('password')
     reppassword = driver.find_element_by_id('repeatpassword')
     gender = driver.find_element_by_id('gender')
     phonenumber = driver.find_element_by_id('phonenumber')
     address = driver.find_element_by_id('address')
     birthdate  = driver.find_element_by_id('dateofbirth')
     bloodgroup  = driver.find_element_by_id('bloodgroup')
     submit = driver.find_element_by_id('submit')
    

     uname.send_keys('chompa')
     username.send_keys('chompa@gmail.com')
     password.send_keys('chompa')
     reppassword.send_keys('chompa')
     gender.send_keys('Female')
     phonenumber.send_keys('014626351')
     address.send_keys('Dhaka')
     birthdate.send_keys('10/04/2000')
     bloodgroup.send_keys('O+')
     submit.send_keys(Keys.RETURN)

  
