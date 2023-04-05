
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

base_url = 'https://moodle.ifsc.edu.br/'


@given(u'acesso a pagina inicial do Moodle')
def step_impl(context):
    context.driver.get(base_url)



@when(u'faço login no sistema')
def step_impl(context):
    actions = ActionChains(context.driver)
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'username'))).send_keys('manoel.f2002')
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys('Manoel1010')
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(1)
    

@when(u'clico no menu Meus Cursos')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/header[2]/nav/div/div/ul[1]/li[2]/a'))).click()
    time.sleep(1)

   

@when(u'entro na página da matéria Testes de Software')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/header[2]/nav/div/div/ul[1]/li[2]/ul/li[6]/a'))).click()
    time.sleep(1)


@when(u'me desespero ao ver um trabalho para dia 05/4')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/section[1]/div/div/ul/li[10]/div[3]/ul/li/div/div/div[2]/div[1]'))).click()
    time.sleep(1)


@when(u'clico na matéria para retornar a página')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[1]/div/div/nav/ul/li[7]/span[1]/a/span'))).click()
    time.sleep(1)

@when(u'clico na checkmark para marcar a atividade como concluida')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/section[1]/div/div/ul/li[10]/div[3]/ul/li/div/div/div[2]/span/form/div/button'))).click()
    time.sleep(1)
                
@when(u'dou scroll para o topo da página novamente')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(2)

@then(u'retorno a página principal')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div[2]/section[2]/aside[1]/div[2]/div[2]/ul/li/ul/li[1]/p/a/span'))).click()
    time.sleep(1)
    context.nome = WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'action-menu-toggle-0'))).text
