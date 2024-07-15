from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

BTN_REJECT_COOKIES = (By.ID, "adopt-reject-all-button")
SUBMIT_FORM_BUTTON = (By.XPATH, "//button[@type='submit']")
NAME_INPUT = (By.ID, "nome")
EMAIL_INPUT = (By.ID, "email")
SUBJECT_INPUT = (By.ID, "assunto")
MESSAGE_INPUT = (By.ID, "mensagem")

browser = Firefox()
def main() -> None:
  browser.get("https://www.jogajuntoinstituto.org/")
  reject_all_cookes()
  # fill_contact_form(
  #   nome="Rodrigo Molter", 
  #   email="rodrigo.molter@gmail.com", 
  #   mensagem="Olá, humano! BipBop 🤖\n\n Esta mensagem esta sendo enviada de forma automatizada com Selenium Webdriver e Python.", 
  #   assunto="Ser facilitador"
  #   )
  fill_contact_form()
  submit_contact_form()

  WebDriverWait(browser, 15).until(EC.alert_is_present())
  assert browser.switch_to.alert.text == "Dados recebidos!"

  browser.quit()

def reject_all_cookes() -> None:
  WebDriverWait(browser, 5).until(EC.presence_of_element_located(BTN_REJECT_COOKIES))
  browser.find_element(*BTN_REJECT_COOKIES).click()

def fill_contact_form(nome: str = None, email: str = None, assunto: str = None, mensagem: str = None ) -> None:
  fake = Faker()

  nome = nome or fake.name()
  email = email or fake.email()
  assunto = assunto or "Ser facilitador"
  mensagem = mensagem or fake.paragraph()

  browser.find_element(*NAME_INPUT).send_keys(nome)
  browser.find_element(*EMAIL_INPUT).send_keys(email)
  browser.find_element(*MESSAGE_INPUT).send_keys(mensagem)
  Select(browser.find_element(*SUBJECT_INPUT)).select_by_value(assunto)

def submit_contact_form() -> None:
  browser.find_element(*SUBMIT_FORM_BUTTON).click()

main()