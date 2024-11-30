from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://tees.co.id/')

for i in range(2):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]')))
        print('pop up add shown up')
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'btn-modal-close').click()
        print('pop up add closed')
    except TimeoutException:
        print("pop up add didn't shown up")
        pass

    time.sleep(5)