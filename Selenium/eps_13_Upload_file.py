from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# # If tag to upload is 'input' just like in https://demoqa.com/upload-download
# driver.get("https://demoqa.com/upload-download")
# driver.find_element(By.ID, 'uploadFile').send_keys(r'C:\Users\aprin\OneDrive\Pictures\Screenshot 2024-07-29 171148.png')
# time.sleep(10)

# If tag to upload file is a 'button'
import pyautogui
driver.get('https://gofile.io/uploadFiles')
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="filesUpload"]/div/div[1]/div/button').click()
pyautogui.write(r'C:\Users\aprin\OneDrive\Pictures\Screenshot 2024-07-29 171148.png')
time.sleep(3)
pyautogui.press('enter')