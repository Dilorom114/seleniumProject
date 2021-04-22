# 04/18/2021
# Finding the elements:
# by name
# by id (fastest if the element ID is unique)
# by class name
# by link text, by partial link text

# by xpath,
# by css selector

# https://www.seleniumeasy.com/test/basic-first-form-demo.html
# Searching elements inside the developer tools (xpath):
# //form/div/input[@id="user-message"] - //tag/tag/input[@attribute="value"]
#  or //form/div/input[@placeholder="Please enter your Message"]
# searching the same element with id:
#  #user-message
# However, id="user-message" attribute is not unique
# Functions from selenium


# start the browser
from selenium import webdriver
import time

from utilities import *

driver = webdriver.Chrome()
# implicit wait is defined once when you start the browser and this will apply to all find element steps
driver.implicitly_wait(20)
driver.maximize_window()

def open_website(url):
    '''open the website, and click on 'No, thanks!' button'''
    # url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
    driver.get(url)
    print(f"Title of the page: {driver.title}")
    # time.sleep(2)  # one way of holding the execution and to wait for something
    print("now clicking the 'No thanks!' button")
    driver.find_element_by_link_text('No, thanks!').click()

def back_forward():
    driver.back()
    time.sleep(5)
    print(f"Title of the page 2: {driver.title}")
    # adding the time stamp makes the file name unique
    driver.get_screenshot_as_file(f'screenshots/{get_str_seconds()}_datapage.png')
    driver.forward()
    print(f"Title of the page 3: {driver.title}")
    driver.get_screenshot_as_file(f'screenshots/{get_str_seconds()}_seleniumdemo.png')
    time.sleep(5)

def get_total_input_fileds():
    '''
    find the "Enter a" input box
    find the "Enter b" input box
    enter the "20" text in a
    enter the "30" text in b
    '''
    avalue_input = driver.find_element_by_id('sum1')
    bvalue_input = driver.find_element_by_id('sum2')
    avalue_input.send_keys("20")
    bvalue_input.send_keys("30")

    # find the "Get total" button, then click on that button
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sum_button = driver.find_element_by_xpath("//button[text()='Get Total']")
    sum_button.click()
    driver.get_screenshot_as_file(f'screenshots/{get_str_seconds()}_result.png')

def close_browser():
    driver.close()  # closes the current tab
    driver.quit()  # closes the browser


print("Execution starting....")
# Scenario 1:
url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
open_website(url_inputs)
back_forward()
get_total_input_fileds()
close_browser()

# Scenario 2:
url_checkbox = "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"
open_website(url_inputs)
# create steps to test checkbox using selenium
close_browser()
print("Steps are completed!")



