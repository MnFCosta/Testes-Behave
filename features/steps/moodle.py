
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


#Variavel com a URL do site que iremos acessar
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
    time.sleep(3)
    

""" @when(u'clico no menu Pessoas')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'item_1'))).click()
    time.sleep(3)


@when(u'clico no botão novo')
def step_impl(context):
    #Seta o iframe da tela de pessoas como principal
    context.driver.switch_to.frame(context.driver.find_element(By.ID,'iframe_item_1'))
    context.driver.switch_to.default_content() #para voltar ap frame principal
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'sc_b_new_top'))).click()
    time.sleep(3)


@when(u'Insiro dados de uma nova pessoa')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'nome'))).send_keys('Nome Teste')
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'cep'))).send_keys('83880000')
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'cidade'))).send_keys('Rio Negro')
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'uf'))).send_keys('Paraná')
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'fone01'))).send_keys('47999999999')
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'fone02'))).send_keys('47988888888')
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'data_nascimento'))).send_keys('28021900')
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'email'))).send_keys('eduardo.gomes@ifsc.edu.br')
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'profissao'))).send_keys('Testados de Software')
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'observacao'))).send_keys('Cadastro realizado automaticamente')
    time.sleep(3)


@when(u'clico em salvar')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'sc_b_ins_t'))).click()
    time.sleep(5)

@when(u'clico em voltar')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Voltar'))).click()
    time.sleep(3)


@then(u'A pessoa cadastrada deve ser apresentada no primeiro registro da consulta.')
def step_impl(context):
    context.pessoa = WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'id_sc_field_nome_1'))).text
    if (context.pessoa != 'NOME TESTE'):
        raise Exception('Erro ao cadastrar a pessoa Nome Teste')
    else:
        #Sai do sistema
        context.driver.switch_to.default_content()
        WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'item_13'))).click()
        time.sleep(3) """
        
