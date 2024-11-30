from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)


"""For date input with empty column"""

# driver.get('https://jqueryui.com/datepicker/')
# driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'demo-frame'))

# # Option 1
# driver.find_element(By.ID, 'datepicker').click()
# driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[6]').click()  # element of date
# time.sleep(5)

# Option 2
# driver.find_element(By.ID, 'datepicker').send_keys('02/12/2000')
# time.sleep(5)

# Replace previous date with the new one
# driver.find_element(By.ID, 'datepicker').send_keys('02/12/2000')
# time.sleep(5)
# driver.find_element(By.ID, 'datepicker').clear()
# time.sleep(3)
# driver.find_element(By.ID, 'datepicker').send_keys('09/08/2019')
# time.sleep(5)


""" For data input with default column """

import pyautogui
driver.get('https://demoqa.com/date-picker')
driver.find_element(By.ID, 'datePickerMonthYearInput').click()
pyautogui.press('backspace', presses=10)
time.sleep(4)
driver.find_element(By.ID, 'datePickerMonthYearInput').send_keys('23/05/2023')
time.sleep(5)

