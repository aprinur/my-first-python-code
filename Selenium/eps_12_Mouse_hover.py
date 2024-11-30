from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get('https://demoqa.com/menu')
driver.maximize_window()

""" How to choose Sub Sub Item 1 from Main item 2 -> Sub Sub List in https://demoqa.com/menu """

# Option 1

menu = driver.find_element(By.LINK_TEXT, 'Main Item 2')
sub_menu = ActionChains(driver).move_to_element(menu)
sub_menu.perform()

menu2 = driver.find_element(By.LINK_TEXT, 'SUB SUB LIST »')
sub_sub_menu = ActionChains(driver).move_to_element(menu2)
sub_sub_menu.perform()

menu3 = driver.find_element(By.LINK_TEXT, 'Sub Sub Item 1')
sub_sub_item1 = ActionChains(driver).move_to_element(menu3)
sub_sub_item1.perform()
time.sleep(3)

# Option 2

ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT, 'Main Item 2')).perform()
ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT, 'SUB SUB LIST »')).perform()
ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT, 'Sub Sub Item 1')).perform()
time.sleep(2)

