from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_tovari_dostupni_po_ssilke(browser):
    time.sleep(30)
    dobavitVKorzinu = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")))
    dobavitVKorzinu.click()

    assertProverka = browser.find_element_by_xpath("//strong[contains(text(), 'Coders at Work')]")
    assertProverkatext = assertProverka.text
    assert assertProverkatext == "Coders at Work", "Doljno bit ravno Coders at Work"

    
