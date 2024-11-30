from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://demoqa.com/alerts')

# Handling single button alert
driver.find_element(By.ID, 'alertButton').click()
time.sleep(3)
driver.switch_to.alert.accept()  # code to accept alert
time.sleep(3)

# Handling 2 button alert
driver.find_element(By.ID, 'confirmButton').click()
time.sleep(3)
driver.switch_to.alert.dismiss()  # code to close alert
time.sleep(3)

# Handling alert with promp box
driver.find_element(By.XPATH, '//*[@id="promtButton"]').click()
time.sleep(3)
driver.switch_to.alert.send_keys('Hola')  # code to input and enter from alert
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)