import time

from source.finding_elements import *

print("Execution starting....")

def test_webdriver_input_elements():
    # Scenario 1:
    print("\nScenario #1: WebDriver methods, properties, WebElement methods (input fields)")
    url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
    open_website(url_inputs)
    back_forward()
    get_total_input_fields()

def test_checkbox():
    # Scenario 2:
    print("\nScenario #2: Handling CheckBox")
    url_checkbox = "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"
    open_website(url_checkbox)
    # create steps to test checkbox using selenium
    checkbox_elements()



# driver.get("https://amazon.com")
# host = driver.current_url
# host
# 'https://www.amazon.com/'
# if host == "https://amazon.com":
#     print("yess test passed")
# else:
#     print("noo test failed")
#
# driver.title
# 'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more'
# search_box = driver.find_element_by_id("twotabsearchtextbox")
# search_box.send_keys("kids toys")
# #
# # from selenium.webdriver.common.keys import Keys
# #
# # search_box.send_keys(Keys.RETURN)
# # search_box.clear()

print("Execution starting....")

def test_ecommerse_products_example():
    # Scenario 3
    print("\nScenario #3: working with multiple elements, ecommerse website")
    # go to this website and search the product
    website = "http://automationpractice.com/index.php"
    open_website(website)
    ecommerse_search()
    print("Scenario 3 completed")


def test_amazon_example():
    # Scenario 4: amazon example, find_elements
    amazon_example()


print("closing the browser")
close_browser()
print("Steps are completed!")
