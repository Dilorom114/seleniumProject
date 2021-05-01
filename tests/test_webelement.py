from source.finding_elements import *

print("Execution starting....")
# Scenario 1: Handling the Drop Down List
url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
# add scenario execution lines here


# Scenario 2:
# variables
# call functions from finding_elements.py
# close_browser()
# print("Test webelement steps are completed!")

# explicit_wait_methods()




def test_drop_down():
    # Scenario 5:
    print("\nScenario #5: drop down list")
    drop_down_list()


def test_drop_down_multi_select():
    # Scenario 6:
    print("\nScenario #6: drop down multi select methods")
    drop_down_multi_select()


def test_js_alerts():
    # Scenario 7:
    print("\nScenario #7: handling the js alert")
    swich_to_alert()


def test_pop_up_window():
    # Scenario 8:
    print("\nScenario #8: handling the popup window")
    switch_to_window()


def test_explicit_wait():
    # Scenario 9:
    print("\nScenario #9: explicit wait cases")
    # explicit_wait_methods()


print("closing the browser")
close_browser()
print("Steps are completed!")