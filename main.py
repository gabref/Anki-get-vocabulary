from genericpath import exists
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from simple_image_download import simple_image_download as simp 
# import time

# para abrir o navegador 
# nav = webdriver.Chrome()

# rodar navegador em segundo plano
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True
# nav = webdriver.Chrome(options=chrome_options)

word = 'dog'

# deletar imagens
# def deletarImagens():
    # import os
    # if not os.path.exists('my_folder'):
    #     os.makedirs('my_folder')
    # os.rename('search2.jpg')
    # count = 0
    # while True:
    #     if count == 1:
    #         count = 2
    #     file_name = f'search{count+1}.jpg'
    #     if os.path.exists(file_name):
    #         os.remove(file_name)
    #         count += 1
    #     else:
    #         print("Finished deleting Images")
    #         break

# BAIXAR IMAGENS
def baixarImagens(query):
    response = simp.simple_image_download
    response().download(query, 1)

# response = simp.simple_image_download
# lst=['dog','cat']
# for rep in lst:
#     response().download(rep , 1)
    
baixarImagens(word) # baixar imagens

# nav.quit()

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