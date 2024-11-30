from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()  # maximize window
time.sleep(5)
driver.minimize_window()  # minimize window
time.sleep(5)
