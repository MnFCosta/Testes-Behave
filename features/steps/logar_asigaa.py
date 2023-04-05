
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

base_url = 'https://sigaa.ifsc.edu.br/sigaa/verTelaLogin.do'


@given(u'acesso a pagina inicial do Sigaa')
def step_impl(context):
    context.driver.get(base_url)



@when(u'logo no Sigaa para ver se não tenho outros trabalhos')
def step_impl(context):
    actions = ActionChains(context.driver)
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'user.login'))).send_keys('manoel.f2002')
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'user.senha'))).send_keys('Manoel1010')
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(5)
    

@then(u'saio imediatamente')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="info-sistema"]/div/span[3]/a'))).click()
    time.sleep(2)
