
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


base_url = "https://www.youtube.com/"

@given(u'acesso a pagina inicial do Youtube')
def step_impl(context):
    context.driver.get(base_url)

@when(u'clico no campo de busca')
def step_impl(context):
    action = ActionChains(context.driver)
    search_box = context.driver.find_element(By.XPATH, "//input[@id='search']")
    action.move_to_element(search_box).click()
    action.send_keys("Coyote/Wolf nose boop meme")
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(1)

@when(u'clico no video')
def step_impl(context):
    action = ActionChains(context.driver)
    
    video = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer")))
    action.move_to_element(video).perform()

    WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-image/img"))).click()
    action.perform()
    time.sleep(5)


""" @when(u'clico no video')
def step_impl(context):
    action = ActionChains(context.driver)
    
    video = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer")))
    action.move_to_element(video).perform()

    WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-image/img"))).click()
    action.perform()
    time.sleep(5)
    



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