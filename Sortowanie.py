import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

def Sort(driver):
    select_element = driver.find_element(By.ID, "selectPrductSort2")
    select = Select(select_element)
    select.select_by_value("http://vanaheim.pl/pl/394-w40k-nowosci?orderby=price&orderway=asc")

def ReadPrice(driver):
    product_element = driver.find_element(By.CSS_SELECTOR, '.ajax_block_product')
    price_element = product_element.find_element(By.CSS_SELECTOR, '.pprice span')
    price = price_element.text
    print('Cena pierwszego produktu:', price)


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://vanaheim.pl/pl/394-w40k-nowosci")

time.sleep(2)

ReadPrice(driver)
Sort(driver)
time.sleep(2)
ReadPrice(driver)

driver.quit()

