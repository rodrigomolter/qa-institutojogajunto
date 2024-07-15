from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT = (By.NAME, "q")
SEARCH_RESULTS = (By.CSS_SELECTOR, "#search a h3")

browser = Firefox()

def main() -> None:
  browser.get("https://www.google.com")

  results = google_search_for("Instituto Joga Junto")

  for result in results:
    if result.text == "Instituto Joga Junto":
      result.click()
      break

  assert browser.title == "Instituto Joga Junto", "Título da página não era Instituto Joga Junto"
  browser.quit()

def google_search_for(query: str) -> None:
  browser.find_element(*SEARCH_INPUT).send_keys(f"{query}{Keys.ENTER}")
  WebDriverWait(browser, 5).until(EC.presence_of_element_located(SEARCH_RESULTS))
  return browser.find_elements(*SEARCH_RESULTS)

main()