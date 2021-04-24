from source.finding_elements import *

print("Execution starting....")
# Scenario 1:
url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
# open_website(url_inputs)
# back_forward()
# get_total_input_fileds()
# close_browser()

# Scenario 2:
url_checkbox = "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"
open_website(url_checkbox)
# create steps to test checkbox using selenium
checkbox_test()
close_browser()

print("Steps are completed!")

# Scenario 3:
# go to this website: http://automationpractice.com/index.php
# find the element by id 'search_query_top'
# search for dress
# get the list of products and get the text out of each product
#       use find elements to find products listed, this returns a list
#       loop through this list and use element.text
# check the count of products
#       we have a list of elements, len(products)
# click on last product
#       products[-1]

# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('http://automationpractice.com/index.php')
# srch_box = driver.find_element_by_id('search_query_top')
# srch_box.send_keys('dress')

# prods_xpath = "//ul[@class='product_list grid row']//a[@class='product-name']"
# products = driver.find_element_by_xpath(prods_xpath)
# prod_names = []
# for product in products:
#     prod_names.append(product.text.strip(w)as)

