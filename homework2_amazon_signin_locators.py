from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\Users\jerem\TestAutomation\chromedriver')
driver.get('https://www.amazon.com/')

# Amazon Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Continue Button
driver.find_element(By.ID, "continue")
driver.find_element(By.XPATH, "//input[@class='a-button-input']")

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.ID, "auth-fpp-link-bottom")
driver.find_element(By.XPATH, "//*[@id='auth-fpp-link-bottom']")

# Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")

# Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

# Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_condition_of_use')]")

# Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_privacy_notice')]")