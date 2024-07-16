from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("que estou na página do instituto joga junto")
def step_on_instituto_page(context):
  context.browser = Firefox()
  context.browser.get("https://www.jogajuntoinstituto.org/")

@when("preencho o formulário de contato")
def step_fill_form(context):
  NAME_INPUT = (By.ID, "nome")
  EMAIL_INPUT = (By.ID, "email")
  SUBJECT_INPUT = (By.ID, "assunto")
  MESSAGE_INPUT = (By.ID, "mensagem")

  context.browser.find_element(*NAME_INPUT).send_keys("Rodrigo")
  context.browser.find_element(*EMAIL_INPUT).send_keys("rodrigo@teste.com")
  context.browser.find_element(*MESSAGE_INPUT).send_keys("Olá, humano! BipBop 🤖\n\n Esta mensagem esta sendo enviada de forma automatizada com Selenium Webdriver, Python e Behave.")
  Select(context.browser.find_element(*SUBJECT_INPUT)).select_by_value("Ser facilitador")

@when("aperto o botão de enviar")
def step_submit_form(context):
  SUBMIT_FORM_BUTTON = (By.XPATH, "//button[@type='submit']")
  context.browser.find_element(*SUBMIT_FORM_BUTTON).click()

@then("os dados são recebidos com sucesso")
def step_assert_form_submited_successfully(context):
  WebDriverWait(context.browser, 15).until(EC.alert_is_present())
  assert context.browser.switch_to.alert.text == "Dados recebidos!"
  context.browser.quit()