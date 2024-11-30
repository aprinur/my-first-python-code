from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/nested_frames')

# Getting left frame

driver.switch_to.frame('frame-top')
driver.switch_to.frame('frame-left')

left = driver.find_element(By.XPATH, '/html/body').text
print(left)

# Switch and getting right frame
driver.switch_to.parent_frame()
driver.switch_to.frame('frame-right')
right = driver.find_element(By.XPATH, '/html/body').text
print(right)

# Switch and getting bottom frame
driver.switch_to.parent_frame()
driver.switch_to.parent_frame()
driver.switch_to.frame('frame-bottom')
bottom = driver.find_element(By.XPATH, '/html/body').text
print(bottom)