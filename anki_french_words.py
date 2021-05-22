from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# para abrir o navegador 
# nav = webdriver.Chrome()

# rodar navegador em segundo plano
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True
nav = webdriver.Chrome(options=chrome_options)

# funções do webdriver
# nav.get(url)
# nav.find_element_by_xpath(codigoxpath).send_keys('escrita pra pesquisa')
# nav.find_element_by_xpath(codigoxpath).send_keys(Keys.ENTER)
# variavel = nav.find_element_by_xpath(codigoxpath).get_attribute('data-value')
# variavel = nav.find_element_by_xpath(codigoxpath).text
# nav.quit()
# time.sleep(1)
