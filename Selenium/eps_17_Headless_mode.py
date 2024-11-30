from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--headless=new')

driver = webdriver.Chrome(options=options)
driver.get('https://demoqa.com/')
print(driver.title)

"""Headless mode = the browser window wouldn’t be visible"""