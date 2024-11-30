from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://demoqa.com/alerts')

driver.find_element(By.ID, 'timerAlertButton').click()

try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    time.sleep(3)
    driver.switch_to.alert.accept()
    print('done')
except TimeoutException:
    print("Alert doesn't pop out")
    pass

"""
Condition to be expected:

title_is
title_contains
presence_of_element_located
visibility_of_element_located
fisibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
"""
