# Finding the elements:
# by name
# by id (fastest if the element ID is unique)
# by class name
# by link text, by partial link text

# by xpath,
# by css selector

# Functions from selenium

# start the browser
import time

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
# implicit wait is defined once when you start the browser and this will apply to all find element steps

# open the website, and click on 'No, thanks!' button
url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
driver.get(url)
# time.sleep(2)  # one way of holding the execution and to wait for something
print("now clicking the 'No thanks!' button")
driver.find_element_by_link_text('No, thanks!').click()


# find the "Enter a" input box
# find the "Enter b" input box
avalue_input = driver.find_element_by_id('sum1')
bvalue_input = driver.find_element_by_id('sum2')
# enter the "20" text in a
# enter the "30" text in b
# driver.
avalue_input.send_keys("20")
bvalue_input.send_keys("30")
# find the "Get total" button, then click on it
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sum_button = driver.find_element_by_xpath("//button[text()='Get Total']")
sum_button.click()
# click on that button
# driver.close()  # close the current tab
# driver.quit()  # closes the browser
print("Steps are completed!")