import time, os, requests
from conf import USERNAME, PASS # importing cretials from conf.py
from selenium import webdriver
browser = webdriver.Chrome() # selecting browser type
url = "https://mygradschool.uncc.edu/"

browser.maximize_window()
browser.get(url)

time.sleep(2)
uname_el = browser.find_element_by_name("username")
uname_el.send_keys(USERNAME)

pass_el = browser.find_element_by_name("password")
pass_el.send_keys(PASS)

time.sleep(1.5)

submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
submit_btn_el.click()

time.sleep(2.5)

# TODO: make it a function
# TODO: check for presence
# def check_decision():
# decision_xpath = "//div[contains(@class, 'widget-todo-list-expand collapse')]"
# decision_ele = browser.find_elements_by_xpath(decision_xpath)
# decision_ele.click()

# Creating a new dir to dump the decision letter
base_path = os.path.dirname(os.path.abspath(__file__)) # getting the path name of this file
dir_path  = os.path.join(base_path, 'data') # inserting the new dir within that path 
os.makedirs(dir_path, exist_ok=True) # creting the folder

admit_letter = "//a[contains(@href, 'application/onlineapp.asp?mode=status&aid')]"
admit_letter_ele = browser.find_elements_by_xpath(admit_letter)
for el in admit_letter_ele:
    admit_href = el.get_attribute("href")
    time.sleep(1)
    browser.get(admit_href)
    myfile = requests.get(admit_href)
    open(dir_path, 'wb').write(myfile.content)
    break