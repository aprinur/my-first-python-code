from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://demoqa.com/droppable')
driver.maximize_window()
driver.implicitly_wait(5)

drag = driver.find_element(By.ID, 'draggable')
drop = driver.find_element(By.ID, 'droppable')

action = ActionChains(driver)
action.drag_and_drop(drag, drop).perform()
time.sleep(10)
