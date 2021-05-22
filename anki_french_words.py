from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# para abrir o navegador 
# nav = webdriver.Chrome()

# rodar navegador em segundo plano
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True
nav = webdriver.Chrome(options=chrome_options)

