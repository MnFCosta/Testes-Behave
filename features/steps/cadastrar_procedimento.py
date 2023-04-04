
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time



""" @when(u'clico no menu Procedimentos')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'item_5'))).click()
    time.sleep(3)

@when(u'clico no botão novo procedimento')
def step_impl(context):
    #Seta o iframe da tela de procedimentos como principal
    context.driver.switch_to.frame(context.driver.find_element(By.ID,'iframe_item_5'))
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'sc_b_new_top'))).click()
    time.sleep(3)


@when(u'insiro dados de um novo procedimento')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="idAjaxSelect_id_pessoa"]/span/span[1]'))).click()
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/span/span/span[1]/input'))).send_keys('NOME TESTE',Keys.ENTER)
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'observacao'))).send_keys('Registro gerado automaticamente')
    time.sleep(3)

@when(u'clico em salvar procedimento')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'sc_b_ins_t'))).click()
    time.sleep(3)

@when(u'clico no botão novo item procedimento')
def step_impl(context):
    #Seta o iframe da tela de procedimentos como principal
    context.driver.switch_to.frame(context.driver.find_element(By.ID,'nmsc_iframe_liga_F002_form_procedimento_servico'))
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'sc_b_new_t'))).click()
    time.sleep(3)


@when(u'insiro dados de um item de procedimento')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="idAjaxSelect_id_servico_1"]/span/span[1]'))).click()
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/span/span/span[1]/input'))).send_keys('CORTE',Keys.ENTER)
    time.sleep(3)
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="idAjaxSelect_id_profissional_1"]/span/span[1]'))).click()
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/span/span/span[1]/input'))).send_keys('FABIANA',Keys.ENTER)
    
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.NAME,'descricao_1'))).send_keys('Registro gerado automaticamente')


@when(u'clico em salvar item procedimento')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'sc_ins_line_1'))).click()
    print()

@when(u'clico em salvar procedimento novamente')
def step_impl(context):
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(context.driver.find_element(By.ID,'iframe_item_5'))
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'sc_b_upd_t'))).click()
    time.sleep(3)


@when(u'clico em voltar para tela procedimento')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Voltar'))).click()
    time.sleep(3)


@then(u'O procedimento cadastrado deve ser apresentada no primeiro registro da consulta.')
def step_impl(context):
    context.pessoa = WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'id_sc_field_id_pessoa_1'))).text
    if (context.pessoa != 'NOME TESTE'):
        raise Exception('Erro ao cadastrar um novo Procedimento')
    else:
        #Sai do sistema
        context.driver.switch_to.default_content()
        WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID,'item_13'))).click()
        time.sleep(3) """