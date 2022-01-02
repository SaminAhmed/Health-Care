import random
import time
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

report = Report()
driver = webdriver.Chrome(
    executable_path="C:\\Users\\sohan\\Downloads\\Compressed\\chromedriver.exe")
report.setup(
    report_folder=r'Reports',
    module_name='Health Care System',
    release_name='Release 1',
    selenium_driver=driver
)
driver.get('http://127.0.0.1:8000')

#Test case 1

try:
    # Start of Test
    report.write_step(
        'Navigate to Admin Login Page',
        status=report.status.Start,
        test_number=1
    )
    login = driver.find_element_by_name("admin_login").click()

    results = driver.current_url
    print(results)
    assert "http://127.0.0.1:8000/admin_login/" == results
    report.write_step(
        'Successfully Navigate to Admin Login',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Naviagte Admin Login',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


#Test case 2

try:
    # Start of Test
    report.write_step(
        'Admin Login Test',
        status=report.status.Start,
        test_number=2
    )
    username = driver.find_element_by_name("username")
    username.send_keys("admin")
    password = driver.find_element_by_name("password")
    password.send_keys("admin")
    driver.find_element_by_name("login_btn").click()
    time.sleep(5)
    driver.switch_to.alert.accept()
    results = driver.current_url
    print(results)
    
    assert "http://127.0.0.1:8000/adminhome/" == results
    report.write_step(
        'Successfully Logged In',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Admin Login',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test case 3

try:
    # Start of Test
    report.write_step(
        'Navigate to Add Receptionist Page',
        status=report.status.Start,
        test_number=3
    )
    obj = driver.find_element_by_name("add_receptionist").click()

    results = driver.current_url
    print(results)
    assert "http://127.0.0.1:8000/adminaddReceptionist/" == results
    report.write_step(
        'Successfully Navigate to Add Receptionist Page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Naviagte Add Receptionist Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


#Test case 4


try:
    # Start of Test
    report.write_step(
        'Add Receptionist',
        status=report.status.Start,
        test_number=4
    )
    name = driver.find_element_by_name("name")
    name.send_keys("Test User")
    rand = random.randint(0, 100)
    email = driver.find_element_by_name("email")
    email.send_keys(str(rand)+"testuser"+str(rand)+"@gmail.com")
    password = driver.find_element_by_name("password")
    password.send_keys("test1234")
    repeatpassword = driver.find_element_by_name("repeatpassword")
    repeatpassword.send_keys("test1234")
    gender = driver.find_element_by_name("gender")
    gender.click()
    gender.send_keys(Keys.DOWN)
    gender.send_keys(Keys.ENTER)  
    phonenumber = driver.find_element_by_name("phonenumber")
    phonenumber.send_keys("+8801888888"+str(rand)) 
    address = driver.find_element_by_name("address")
    address.send_keys("Dhaka, Bangladesh"+str(rand))
    dateofbirth = driver.find_element_by_name("dateofbirth")
    dateofbirth.send_keys("04041998")
    bloodgroup = driver.find_element_by_name("bloodgroup")
    bloodgroup.click()
    bloodgroup.send_keys(Keys.DOWN)
    bloodgroup.send_keys(Keys.ENTER)
    obj = driver.find_element_by_name("add_receptionist_btn").click()
    time.sleep(5)
    results = driver.switch_to.alert.accept()
    time.sleep(5)
    # print(results.text)
    assert True
    report.write_step(
        'Successfully Add Receptionist',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Add Receptionist',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


#Report Generation
report.generate_report()
driver.quit()
