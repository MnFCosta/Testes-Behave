from selenium import webdriver

def before_all(context):
    print("Começando!")
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    context.driver = webdriver.Chrome(options=options)


def before_scenario(context, scenario):
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)

def after_scenario(context,scenario):
    print("Passou!")


def after_all(context):  
    context.driver.quit()

