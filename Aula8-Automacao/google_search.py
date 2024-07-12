from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = Firefox()
browser.get("https://www.google.com")

browser.find_element(By.NAME, "q").send_keys(f"Instituto Joga Junto {Keys.ENTER}")

WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search a h3")))
results = browser.find_elements(By.CSS_SELECTOR, "#search a h3")

for result in results:
  if result.text == "Instituto Joga Junto":
    result.click()
    break

assert browser.title == "Instituto Joga Junto", "Título da página não era Instituto Joga Junto"
browser.quit()