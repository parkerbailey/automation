from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# FUNCTION DEFINITIONS
def extract_list_items(element_list):
    content = []
    for i in element_list: content.append(i.get_attribute("textContent").strip())
    return content

# initialize webdriver
driver = webdriver.Firefox()

# navigate to search page
driver.get("https://www.classic.com/search?q=")
sleep(10)

# open filters
driver.find_element(By.CSS_SELECTOR, "button.text-gray-500:nth-child(1) > div:nth-child(1) > span:nth-child(2)").click()
sleep(3)

# makes
driver.find_element(By.CSS_SELECTOR, ".gap-5 > div:nth-child(1) > a:nth-child(3)").click() # expand to all makes
sleep(3)
makes = extract_list_items(driver.find_element(By.CSS_SELECTOR, ".gap-5 > div:nth-child(1) > div:nth-child(2)").find_elements(By.CLASS_NAME, "text-base"))

breakpoint()
driver.quit()

# doors

# driver side

# ext color

# int color

# originality

# vehicle type

# countires

