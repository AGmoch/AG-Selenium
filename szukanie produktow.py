import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys



def Search(driver, product):
    driver.find_element("id", "search_query_top").send_keys(product)
    search_box = driver.find_element(By.ID, "search_query_top")
    search_box.send_keys(Keys.RETURN)

def Count(driver):
    elements = driver.find_elements(By.CSS_SELECTOR, ".categorie_product li")
    count = len(elements)
    return count

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

product = "Resident Evil 3"

driver.get("https://vanaheim.pl/pl/")

Search(driver, product)
time.sleep(2)

result_count = Count(driver)
if result_count == 3:
    print("Liczba znalezionych elementów:", result_count)
    print("Wszystko udało się znaleźć!")
else:
    print("Error: Nie znaleziono oczekiwanej liczby elementów.")

time.sleep(2)

driver.quit()