from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get('https://www.google.com/')

# # Locating element and doing action with find_element() (single result)
""" Adjust locating method based on element in the website  """

element1 = driver.find_element(By.CLASS_NAME, 'gLFyf')  # by class
element1.send_keys('Hello World', Keys.ENTER)  # input and enter
time.sleep(5)

element2 = driver.find_element(By.ID, 'APjFqb')  # by id
element2.send_keys('Python', Keys.ENTER)  # input and enter
time.sleep(5)

element3 = driver.find_element(By.LINK_TEXT, 'Gmail')  # by link_text (get the text not the link)
time.sleep(5)
element3.click()  # click element

element4 = driver.find_element(By.XPATH, "//*[@id='gb']/div/div[1]/div/div[2]/a")  # by  xpath
time.sleep(5)
element4.click()  # click element
time.sleep(2)

element5 = driver.find_element(By.CSS_SELECTOR, '#gb > div > div:nth-child(1) > div > div:nth-child(2) > a')
time.sleep(5)
element5.click()
time.sleep(5)

""" Semua selection method bisa digunakan pada find_element() dan find_elements()"""



