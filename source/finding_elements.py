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
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

from utilities import *

# this will disable adds, unwanted popups
options = Options()
options.add_argument('--disable-notifications')
options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=options)

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


def drop_down_list():
    pass
    url_ddown = "https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html"
    driver.get(url_ddown)
    driver.refresh()
    ddown_list = driver.find_element_by_id("select-demo")
    print("Different...")
    selection = Select(ddown_list)
    selection.select_by_visible_text("Tuesday")
    selection.select_by_index(5)
    selection.select_by_value("Monday")

    print("options method: returns list of options in the drop down")
    for element in selection.options:
        print(element.text)

    print("first_selected_option: returns element select")
    print(selection.first_selected_option.text)
    print("all_selected_options: returns selected option(s):")
    for element in selection.all_selected_options:
        print(element.text)


def drop_down_multi_select():
    url_dropdown = "https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html"
    driver.get(url_dropdown)
    ddown_list = driver.find_element_by_id("multi-select")  # Select element with '<select>' tag
    selection = Select(ddown_list)

    #Multi select drop down enables you to select multi options
    selection.select_by_value("New York")
    selection.select_by_visible_text("Ohio")
    print("selection.all_selected_options :")
    for element in selection.all_selected_options:
        print(element.text)  # this will return all selected options (new york, ohio)
    print("Deselecting by index: ")
    selection.deselect_by_index(4)

    selection.select_by_index(5)
    selection.select_by_index(7)
    print("Deselecting_all: ")
    selection.deselect_all()

def swich_to_alert():
    driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
    driver.find_element_by_xpath("//button[@onclick='myAlertFunction()']").click()
    alert = driver.switch_to.alert
    print(alert.text)  # 'I am an alert box!'
    print("Clicking the OK button")
    alert.accept()
    print("***** handling alerts with multiple buttons ***** ")
    driver.find_element_by_xpath("//button[@onclick='myPromptFunction()']").click()
    alert2 = driver.switch_to.alert
    alert2.send_keys("John Doe")  # this did not work

    print("Clicking the CANCEL button")
    alert2.dismiss()
    driver.find_element_by_xpath("//button[@onclick='myPromptFunction()']").click()
    alert2.send_keys("John Doe")
    print(alert2.text)  # 'Please enter your name'
    alert2.accept()

def switch_to_window():
    driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
    print(" ******** switching to window ********")
    email_locator = '//input[@name="session[username_or_email]"]'
    url_window_popup = "https://www.seleniumeasy.com/test/window-popup-modal-demo.html"
    twt_xpath = '//a[@title="Follow @seleniumeasy on Twitter"]'
    driver.get(url_window_popup)

    driver.get(url_window_popup)
    print("This is the unique id of current tab/window: ")
    driver.current_window_handle # 'CDwindow-376884978E3D6EAD4E8A76FDB1CBDCE0'
    main_window = driver.current_window_handle # we are saving this unique ID so we can come back to this window
    driver.find_element_by_xpath(twt_xpath).click()
    print("listing all unique id of all windows open:")
    driver.window_handles  # ['CDwindow-376884978E3D6EAD4E8A76FDB1CBDCE0', 'CDwindow-54BE1A404685F587B6F62CA7C2B1989E']
    handles = driver.window_handles # we can save in all ids in the list
    print("switching to the second window, this will be second element from the handles list.")
    driver.switch_to.window(handles[1])

    print("finding the email input and entering the email on the second window.")
    email_input = driver.find_element_by_xpath(email_locator)
    email_input.send_keys("myawesomeemail@gmail.com")

    print("switching the focus back to main window")
    driver.switch_to.window(handles[0])
    print("switching the focus to second window, twitter window.")
    driver.switch_to.window(handles[1])
    email_input = driver.find_element_by_xpath(email_locator)
    email_input.send_keys(Keys.TAB)
    pass_locator = '//input[@name="session[password]"]'
    pass_input = driver.find_element_by_xpath(pass_locator)
    pass_input.send_keys("mypassword")
    print('switching the window is completed.')






