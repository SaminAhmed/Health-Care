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
        'Navigate to Login Page',
        status=report.status.Start,
        test_number=1
    )
    login = driver.find_element_by_name("login").click()

    results = driver.current_url
    print(results)
    assert "http://127.0.0.1:8000/login/" == results
    report.write_step(
        'Successfully Navigate to Login',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Naviagte Login',
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
        'Login Test',
        status=report.status.Start,
        test_number=2
    )
    username = driver.find_element_by_name("email")
    username.send_keys("saidur.rahman2@northsouth.edu")
    password = driver.find_element_by_name("password")
    password.send_keys("1234")
    driver.find_element_by_name("login_btn").click()
    time.sleep(5)
    driver.switch_to.alert.accept()
    results = driver.current_url
    print(results)
    
    assert "http://127.0.0.1:8000/home/" == results
    report.write_step(
        'Successfully Logged In',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Login',
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
        'Doctor Profile View',
        status=report.status.Start,
        test_number=3
    )
    driver.find_element_by_name("profile").click()
   
    results = driver.current_url
    print(results)
    
    assert "http://127.0.0.1:8000/profile/" == results
    report.write_step(
        'Successfully View Profile',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to View Profile',
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
        'Doctor View Appointments',
        status=report.status.Start,
        test_number=4
    )
    driver.find_element_by_name("view_app").click()
   
    results = driver.current_url
    print(results)
    
    assert "http://127.0.0.1:8000/viewappointments/" == results
    report.write_step(
        'Successfully View Appointments',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to View Appointments',
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
