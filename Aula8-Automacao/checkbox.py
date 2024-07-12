from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

browser = Firefox()

link = "https://page-test-selenium.s3.sa-east-1.amazonaws.com/index.html"

browser.get(link)

btn_new_element = browser.find_element(By.ID, "addElement")

for _ in range(10):
  btn_new_element.click()


checkboxes = browser.find_elements(By.TAG_NAME, "input")

for checkbox in checkboxes:
  checkbox.click()


browser.quit()