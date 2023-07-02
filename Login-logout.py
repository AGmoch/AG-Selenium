import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def login(driver, username, password):
    button = driver.find_element(By.CSS_SELECTOR, ".header_links")
    button.click()
    driver.find_element("id", "email").send_keys(username)
    driver.find_element("id", "passwd").send_keys(password)
    button = driver.find_element("name", "SubmitLogin")
    button.click()

def logout(driver):
    logout_button = driver.find_element(By.PARTIAL_LINK_TEXT, "WYLOGUJ")
    logout_button.click()


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

username = "kaperif166@fitwl.com"
password = "kaperif166@fitwl.com"

driver.get("https://vanaheim.pl/pl/")

login(driver, username, password)

wait = WebDriverWait(driver, 10)
logout_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "WYLOGUJ")))

logout(driver)
time.sleep(2)

driver.quit()