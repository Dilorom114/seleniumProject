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
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from utilities import *

# this will disable adds, unwanted popups
options = Options()
options.add_argument('--disable-notifications')
# options.add_argument('--headless')  # running the chrome on the background

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


def checkbox_elements():
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
    url_dropdown = "https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html"
    driver.get(url_dropdown)
    driver.refresh()
    ddown_list = driver.find_element_by_id("select-demo")  # Select element
    selection = Select(ddown_list)  # object to represent your drop down on UI
    print("Different ways of selecting from drop down list: ")
    selection.select_by_visible_text("Tuesday")
    selection.select_by_index(5)
    selection.select_by_value("Monday")

    print("options method: returns list of options in the drop down")
    for element in selection.options:
        print(element.text)

    print("first_selected_option: returns element firstly selected ")
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
    print("Deselecting_all : ")
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
    print("This is the unique id of current tab/window: ")
    driver.current_window_handle  # 'CDwindow-376884978E3D6EAD4E8A76FDB1CBDCE0'
    main_window = driver.current_window_handle # we are saving this unique ID so we can come back to this window
    driver.find_element_by_xpath(twt_xpath).click()  # this opens a new window
    print("Listing all unique ids of all windows open:")
    driver.window_handles  # ['CDwindow-376884978E3D6EAD4E8A76FDB1CBDCE0', 'CDwindow-54BE1A404685F587B6F62CA7C2B1989E']
    handles = driver.window_handles # we can save all ids in the list
    print("switching to the second window, this will be the second element from the handles list.")
    driver.switch_to.window(handles[1])

    print("finding the email input and entering the email on the second window.")
    email_input = driver.find_element_by_xpath(email_locator)
    email_input.send_keys("myawesomeemail@gmail.com")

    print("switching the focus back to main window")
    driver.switch_to.window(handles[0])
    print("switching the focus to the second window, twitter window.")
    driver.switch_to.window(handles[1])
    email_input = driver.find_element_by_xpath(email_locator)
    email_input.send_keys(Keys.TAB)
    pass_locator = '//input[@name="session[password]"]'
    pass_input = driver.find_element_by_xpath(pass_locator)
    pass_input.send_keys("mypassword")
    driver.switch_to.window(handles[0])
    print('switching the window is completed.')


# def explicit_wait_methods():
#     url = "https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"
#     # click button: # populate-text
#     # explicitly wait until
#     # text_to_be_present_in_element(
#     # driver.find_element_by_xpath("//h2[@id='h2' and text()='Selenium Webdriver']") -- not good
#     msg_xpath ="////h2[@id='h2']"
#     msg_id = "h2"
#     msg_css_selector = "#h2"
#     locator1 = (By.XPATH, msg_xpath)
#     # WebDriverWait(driver, 60).until(expected_conditions.text_to_be_present_in_element((By.XPATH, msg_xpath), extd_txt))
#
#     extd_txt = "Selenium Webdriver"
#     wdwait = WebDriverWait(driver, 60)
#     driver.get(url)
#     element = driver.find_element_by_id("populate-text")
#     # print(driver.find_element_by_xpath(msg_xpath))3
#     # element.click()
#     # print("waiting untill expected text to appear...")
#     msg = wdwait.until(EC.text_to_be_present_in_element((By.XPATH, msg_xpath), extd_txt))
#     # print(f"did messgae appear now?: {msg}")
#     # print(f"expected message text: {msg}")
#
#
#
#     display_btn_id = "display-other-button"
#     driver.find_element_by_id(display_btn_id).click()
#     print("waiting until enabled button appears... ")
#     enabled_btn = wdwait.until(EC.visibility_of_element_located((By.ID, 'hidden')))
#     enabled_btn.click()
#     print("wait until enabled button disappears...")
#     wdwait.until_not(EC.visibility_of_element_located((By.ID, 'hidden')))
#     print("case 2 completed")

def drag_drop_action():
    pass
    url = "https://www.globalsqa.com/demo-site/draganddrop/"
    driver.get(url)
    time.sleep(5)
    print("Identifying the source and target elements...")
    elem1 = driver.find_element_by_xpath("//img[@src='images/high_tatras_min.jpg']")
    elem2 = driver.find_element_by_xpath("//img[@src='images/high_tatras2_min.jpg']")
    elem3 = driver.find_element_by_xpath("//img[@src='images/high_tatras3_min.jpg']")
    elem4 = driver.find_element_by_xpath("//img[@src='images/high_tatras4_min.jpg']")

    drop_area = driver.find_element_by_xpath("//div[@id='trash']")
    actions = ActionChains(driver)
    actions.drag_and_drop(elem1, drop_area)
    # actions.click_and_hold(elem1).perform

def drag_drop_action3():
    driver.get("http://testautomationpractice.blogspot.com/")
    item1 = driver.find_element_by_xpath("//div[@id='draggable']")
    drop_zone = driver.find_element_by_xpath("//div[@id='droppable']")

    actions = ActionChains(driver)
    actions.drag_and_drop(item1, drop_zone).perform()
    # actions.move_to_element(item1, drop_zone).perform() # hover over element (mouse movement)
    time.sleep(5)
    print("drag and drop finished.")

def move_mouse_action():
    driver.get("http://automationpractice.com/index.php")
    prod_xpath = '//ul[@id="homefeatured"]//a[@title="Faded Short Sleeve T-shirts" and @class="product-name"]'
    driver.execute_script("window.scrollTo(0, 700);")
    time.sleep(5)

    prod1 = driver.find_element_by_xpath(prod_xpath)
    actions = ActionChains(driver)
    actions.move_to_element(prod1)

    time.sleep(10)






