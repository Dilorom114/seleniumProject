from source.finding_elements import *

print("Execution starting....")
# Scenario 1:
url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
open_website(url_inputs)
back_forward()
get_total_input_fields()
# close_browser()

# Scenario 2:
url_checkbox = "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"
open_website(url_checkbox)
# create steps to test checkbox using selenium
checkbox_test()
# close_browser()


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



# Scenario 3: working with multiple elements, ecommerse website
# go to this website
print("Scenario 3 started")
website = "http://automationpractice.com/index.php"
open_website(website)
ecommerse_search()
print("Scenario 3 completed")
# close_browser()

# Scenario 4: amazon example, find_elements
amazon_example()
print("Steps are completed!")





