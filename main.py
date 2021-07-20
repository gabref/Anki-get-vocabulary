from simple_image_download import simple_image_download as simp 
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from urllib import request
import pathlib
import time
import os

# para abrir o navegador 
nav = webdriver.Chrome()

# rodar navegador em segundo plano
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True
# nav = webdriver.Chrome(options=chrome_options)

# VARIAVEL COM O PATH PARA OS ARQUIVOS E CRIA DIRETÓRIO 'MEDIA' SE NÃO JÁ EXISTIR
caminho = pathlib.Path().resolve()
pathScript = str(caminho).replace('\\','/')
dirname = caminho / 'media'
if not dirname.exists():
    os.mkdir(dirname)

word = 'cat'

# BAIXAR IMAGEM
def baixarImagem(query):
    response = simp.simple_image_download
    response().download(query, 1)

# TRANSLATE WORD
def translate_word(query):
    word_pairs = []
    input_language = 'en'
    output_language = 'fr'
    url = f'https://translate.google.com/?sl={input_language}&tl={output_language}&text={query}&op=translate'
    nav.get(url)
    time.sleep(1)
    all_spans = nav.find_elements_by_xpath("//span[@class='VIiyi']") #class for the translated words in google translator
    for span in all_spans:
        word_pairs.append(span.text)
    return word_pairs

#  IPA 
def ipa(query):
    url = 'https://easypronunciation.com/fr/practice-french-pronunciation-online'
    nav.get(url)
    time.sleep(1)
    nav.find_element_by_xpath('//*[@id="custom_word_list"]').send_keys(query)
    nav.find_element_by_xpath('//*[@id="submit"]').click()
    time.sleep(1)
    ipa_word_from_site = nav.find_element_by_xpath('//*[@id="npTitle"]').text
    ipa_word = ipa_word_from_site.split('\n')[-1]
    return ipa_word

# AUDIO
def audio(query, translated_for_path):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"}
    url = f'https://www.collinsdictionary.com/dictionary/english-french/{query}'
    nav.get(url)
    link = nav.find_element_by_xpath('//*[@id="dog__1"]/div[4]/div[1]/div[1]/span[4]/a').get_attribute('data-src-mp3')
    path = pathScript + '/media/' + translated_for_path + '.mp3'
    try:
        req = request.Request(link, headers=headers)
        data = request.urlopen(req).read()
        with open(path, 'wb') as f:
            f.write(data)
            f.close()
    except Exception as e:
        print(str(e))

    
baixarImagem(word) # baixar imagens
# translate_word(word)
# ipa(word) #translated word
# audio(word, 'chien') # english + translation

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