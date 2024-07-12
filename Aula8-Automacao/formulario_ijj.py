from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = Firefox()

browser.get("https://www.jogajuntoinstituto.org/")

WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "adopt-reject-all-button")))
browser.find_element(By.ID, "adopt-reject-all-button").click()

browser.find_element(By.ID, "nome").send_keys("Rodrigo Molter")
browser.find_element(By.ID, "email").send_keys("rodrigo.molter@gmail.com")
browser.find_element(By.ID, "mensagem").send_keys("Olá, humano! BipBop 🤖\n\n Esta mensagem esta sendo enviada de forma automatizada com Selenium Webdriver e Python.")
Select(browser.find_element(By.ID, "assunto")).select_by_value("Ser facilitador")

browser.find_element(By.XPATH, "//button[@type='submit']").click()

WebDriverWait(browser, 15).until(EC.alert_is_present())
assert browser.switch_to.alert.text == "Dados recebidos!"

browser.quit()