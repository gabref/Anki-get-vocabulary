from genericpath import exists
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from simple_image_download import simple_image_download as simp 
import time

# para abrir o navegador 
nav = webdriver.Chrome()

# rodar navegador em segundo plano
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True
# nav = webdriver.Chrome(options=chrome_options)

words = [ 'happiness','girl','dog','boy']
words_t = []

# BAIXAR IMAGENS
def baixarImagens(query):
    response = simp.simple_image_download
    for element in query:
        response().download(element, 1)

# TRANSLATE WORDS
def translate_words(query):
    words_pairs = []
    input_language = 'en'
    output_language = 'fr'
    for element in query:
        url = f'https://translate.google.com/?sl={input_language}&tl={output_language}&text={element}&op=translate'
        nav.get(url)
        time.sleep(1)
        all_spans = nav.find_elements_by_xpath("//span[@class='VIiyi']") #class for the translated words in google translator
        for span in all_spans:
            words_pairs.append(span.text)
        words_t.append(words_pairs)
    
    print(words_t)

# print(word_translated)
    
# baixarImagens(words) # baixar imagens
translate_words(words)

nav.quit()

# funções do webdriver
# nav.get(url)
# nav.find_element_by_xpath(codigoxpath).send_keys('escrita pra pesquisa')
# nav.find_element_by_xpath(codigoxpath).send_keys(Keys.ENTER)
# variavel = nav.find_element_by_xpath(codigoxpath).get_attribute('data-value')
# variavel = nav.find_element_by_xpath(codigoxpath).text
# navegador.find_element_by_xpath('paraclicarnobotao').click()
# nav.quit()
# time.sleep(1)

# import pandas as pd
# tabela = pd.read_excel('nomearquivo')
# tabela.loc[linhas, colunas]
# tabela.loc[tabela['nomeColuna'] == 'valor celulas da linha', 'coluna'] = float(uma variavel)
# # Passo 2: atualizar o preço base reais -> cotação * preço base original
# tabela_produtos['Preço Base Reais'] = tabela_produtos['Cotação'] * tabela_produtos['Preço Base Original']
# # Passo 3: atualizar o preço final -> preço base reais * ajuste
# tabela_produtos['Preço Final'] = tabela_produtos['Preço Base Reais'] * tabela_produtos['Ajuste']
# tabela_produtos['Preço Final'] = tabela_produtos['Preço Final'].map("{:.2f}".format)
# # EXPORTAR NOVA BASE DE DADOS
# tabela_produtos.to_excel('Produtos Atualizados.xlsx', index=False)
# # problemas de tipo de informação
# tabela_clientes['TotalGasto'] = pd.to_numeric(tabela_clientes['TotalGasto'],errors="coerce")
# # problemas de valores vazios
# tabela_clientes = tabela_clientes.dropna(how='all', axis=1)
# tabela_clientes = tabela_clientes.dropna(how='any', axis=0) # excluir linhas vazias
# # itera os itens no arquivo csv para colocar na lista
# for index, row in email_destino.iterrows():
#     conjunto_emails.append(row['email'])