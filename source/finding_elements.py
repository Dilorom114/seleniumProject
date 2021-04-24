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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from utilities import *

driver = webdriver.Chrome()
# implicit wait is defined once when you start the browser and this will apply to all find element steps
driver.implicitly_wait(5)
driver.maximize_window()

def open_website(url):
    '''open the website, and click on 'No, thanks!' button'''
    try:
        # url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
        driver.get(url)
        print(f"Title of the page 1: {driver.title}")
        # time.sleep(2)  # one way of holding the execution and to wait for something
        print("now clicking the 'No thanks!' button..")
        driver.find_element_by_link_text('No, thanks!').click()
    except NoSuchElementException as err:
        print(f"pop did not appear this time.\n{err}")


def back_forward():
    img1 = f'./../screenshots/{get_str_seconds()}_datapage.png'
    img2 = f'./../screenshots/{get_str_seconds()}_seleniumdemo.png'
    driver.back()
    time.sleep(5)
    print(f"Title of the page 2: {driver.title}")
    # adding the time stamp makes the file name unique
    driver.get_screenshot_as_file(img1)
    driver.forward()
    print(f"Title of the page 3: {driver.title}")
    driver.get_screenshot_as_file(img2)
    time.sleep(5)

def get_total_input_fields():
    '''
    find the "Enter a" input box
    find the "Enter b" input box
    enter the "20" text in a
    enter the "30" text in b
    '''
    img1 = f'./../screenshots/{get_str_seconds()}_result.png'

    avalue_input = driver.find_element_by_id('sum1')
    bvalue_input = driver.find_element_by_id('sum2')
    avalue_input.send_keys("20")
    bvalue_input.send_keys("30")

    # find the "Get total" button, then click on that button
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sum_button = driver.find_element_by_xpath("//button[text()='Get Total']")
    sum_button.click()
    driver.get_screenshot_as_file(img1)

def close_browser():
    driver.close()  # closes the current tab
    driver.quit()  # closes the browser


def checkbox_test():
    # todo: code here
    # find the element (using xpath) to check, and click
    check_xpath = "//input[@id='isAgeSelected']"

    print("checkbox test started ...")
    checkbox = driver.find_element_by_xpath(check_xpath)
    checkbox.click()
    time.sleep(5)

    # verify the checkbox is checked
    print(f"Is Checkbox selected (True/False)?: {checkbox.is_selected()}")

    # find the message element and get text
    msg_css_selector = "#txtAge"
    msg = driver.find_element_by_css_selector(msg_css_selector)
    msg_text = msg.text
    print(f"Final message: {msg_text}")

    assert "Success" in msg_text

def ecommerse_search():

    # find the element by id 'search_query_top'
    # search for dress (hit enter or click on search button)

    srch_box = driver.find_element_by_id("search_query_top")
    srch_box.send_keys("dress")
    srch_box.send_keys(Keys.RETURN)
    time.sleep(5)

    # get the list of products and get the text out of each product
    #       use find elements to find products listed, this returns a list named 'products'
    #       loop through this list and use element.text
    # check the count of products
    prods_xpath = "//ul[@class='product_list grid row']//a[@class='product-name']"
    products = driver.find_elements_by_xpath(prods_xpath)  # list
    prod_names = []
    for product in products:
        prod_names.append(product.text.strip())

    #       we have a list of elements, len(products)
    print(f"We have {len(products)} products listed.")
    # click on last product >  products[-1]
    products[-1].click()
    driver.refresh()


def amazon_example():
    """
    demonstrates some methods from WebDriver Class.
    (current_url, driver.title, driver.clear,
    """
    # driver = webdriver.Chrome()
    host = "https://www.amazon.com/"
    driver.get(host)
    host = driver.current_url # this will return the current page url

    print(host)  # 'https://www.amazon.com/'
    if driver.current_url == host:
        print("yess test passed")
    else:
        print("noo test failed")

    print(f"Title of the current page: {driver.title}")
    'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more'
    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys("kids toys")

    search_box.send_keys(Keys.RETURN)
    search_box.clear()