from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')

driver.find_element(By.LINK_TEXT, 'Click Here').click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])  # return to tab 0 in browser window
time.sleep(5)
driver.find_element(By.LINK_TEXT, 'Click Here').click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])  # return to tab 1 in browser window
time.sleep(5)

