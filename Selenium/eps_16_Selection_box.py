from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyautogui
import time


driver = webdriver.Chrome()
driver.get('https://demoqa.com/select-menu')


""" Old style select menu"""

# option = Select(driver.find_element(By.ID, 'oldSelectMenu'))
#
''' choose one '''
# option.select_by_visible_text('Voilet')
# option.select_by_value('8')
#
# time.sleep(5)


""" New style select menu"""

# driver.find_element(By.XPATH, '//*[@id="selectOne"]/div/div[1]').click()
# pyautogui.typewrite('Mr.')
# pyautogui.press('enter')
# time.sleep(5)

""" Multiselect drop down """

driver.find_element(By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[1]').click()
pyautogui.typewrite('Blue')
pyautogui.press('enter')
pyautogui.typewrite('Black')
pyautogui.press('enter')
pyautogui.typewrite('Red')
pyautogui.press('enter')
time.sleep(5)