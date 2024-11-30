from selenium import webdriver

""" Screen shoot in headless mode"""

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # to remove dev ops from the picture
options.add_argument('--headless=new')

driver = webdriver.Chrome(options=options)
driver.get('https://demoqa.com/')
driver.get_screenshot_as_file('screenshot_1_from_eps_18.png')


""" Screen shoot in head mode"""

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])  # to remove dev ops from the picture
option.add_argument('--window-size=1920,1080')  # to get full size image
driver = webdriver.Chrome(options=option)
driver.get('https://jqueryui.com/')
driver.get_screenshot_as_file('screenshot_2_from_eps_18.png')