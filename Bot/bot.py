import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time 

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

browser = webdriver.Chrome(executable_path = DRIVER_BIN)
browser.get("http://url.is/")

ac = ActionChains(browser)

start_button = browser.find_element_by_class_name('start-btn')
ac.move_to_element(start_button).click().perform()

byrja_button = browser.find_element_by_class_name('byrja-btn')
ac.move_to_element(byrja_button).click().perform()

running = True
while running:
    chosen = browser.find_elements_by_class_name('chosen')
    if len(chosen) > 0:
        time.sleep(0.3)
        for c in chosen:
            c.click()
            time.sleep(0.01)

