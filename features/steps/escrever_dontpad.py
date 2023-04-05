
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import string
import time

base_url = 'https://dontpad.com/'

alfabeto = string.ascii_letters + string.digits
string_aleatoria = ''.join(random.choices(alfabeto, k=12))

@given(u'acesso a pagina inicial do Dontpad')
def step_impl(context):
    context.driver.get(base_url)



@when(u'entro numa pagina aleatoria')
def step_impl(context):
    actions = ActionChains(context.driver)
    
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'path'))).send_keys(string_aleatoria)
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(5)
    

@then(u'escrevo algo na pagina')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'text'))).send_keys("EU ESTIVE AQUI :)")
    time.sleep(2)
   


