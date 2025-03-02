from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pandas as pd

# FUNCTION DEFINITIONS
def extract_list_items(element_list: list, descriptor: str):
    """
    Extracts text content from a list of web elements and returns the list.

    element_list:   a list of web elements (Selenium e.g.: driver.find_elements(...))\n
    df:             a Pandas DataFrame containing the text content of each web element as strings
    """
    content = []
    for i in element_list: content.append(i.get_attribute("textContent").strip().split('(', 1)[0])
    df = pd.DataFrame(content, columns=[descriptor])
    return df

def user_select(options, descriptor: str):
    """
    Prompts for user selection from a list of options.

    options:    a list of string options for the user to choose from.\n
    descriptor: a string describing the type of option being selected.\n
    selection:  the resulting individual list item string that was selected by the user.
    """
    print(options.to_string())
    selection = input(f"Enter the number corresponding to the {descriptor} from the above list of options: ")
    return selection

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
df = extract_list_items(driver.find_element(By.CSS_SELECTOR, ".gap-5 > div:nth-child(1) > div:nth-child(2)").find_elements(By.CLASS_NAME, "text-base"), "make")
make = user_select(df, "make")
print("Selection: ", df.iloc[int(make)]['make'])
breakpoint()
driver.quit()

# doors

# driver side

# ext color

# int color

# originality

# vehicle type

# countires

