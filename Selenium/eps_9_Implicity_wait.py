from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(5)  # how to use implicitly_wait. 5 = 5 seconds
driver.get('https://demoqa.com/login')
driver.get('https://demoqa.com/books')
driver.find_element(By.ID, 'login').click()

""" Implicity_wait use to wait until the element we're looking for shown up. 
Implicity wait usualy used in case we have a bad connection. Implicitly_wait() will automaticly
active for every time we use open url"""