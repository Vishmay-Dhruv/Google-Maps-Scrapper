import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/maps")
try:
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_input.clear()
    search_input.send_keys("restaurants in New York")
    search_input.send_keys(Keys.ENTER)

    results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@role='feed']"))
    )
except TimeoutException:
    print("Loading took too much time!")
finally:
    time.sleep(5)
    driver.quit() 