from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.classic.com/")
breakpoint()
driver.quit()