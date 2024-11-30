from selenium import webdriver

options = webdriver.ChromeOptions()

""" In case there is an error from the device but doesn't interfere the automation process, add 
    this code and pass it to parameter 'options=' from the browser when creating instance"""
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.get('https://demoqa.com/')
