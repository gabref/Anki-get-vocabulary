from simple_image_download import simple_image_download as simp 
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from urllib import request
import pathlib
import shutil
import time
import csv
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

# VARIÁVEIS DOS FILES
english_words_file = r'D:\memor\Documents\Programming\Python\Projetos\Anki_Vocabulary\English_Words.csv'
anki_words_file = r'D:\memor\Documents\Programming\Python\Projetos\Anki_Vocabulary\Anki_Words.csv'

# BAIXAR IMAGEM
def baixarImagem(query):
    response = simp.simple_image_download
    response().download(query, 1)
    image_anki = f'<img src="{query}.jpeg">'
    return image_anki

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
    if len(word_pairs) == 1: # makes sure that if the variable is a list with only 1 element, turns it to a string
            word_pairs = str(word_pairs)
    return word_pairs

#  IPA 
def ipa(query):
    # verify if 'query' is a list or not, if it is, select the masculin word
    if isinstance(query, list):
        query_word = query[1]
    else:
        query_word = query
    url = 'https://easypronunciation.com/fr/practice-french-pronunciation-online'
    nav.get(url)
    time.sleep(1)
    nav.find_element_by_xpath('//*[@id="custom_word_list"]').clear()
    nav.find_element_by_xpath('//*[@id="custom_word_list"]').send_keys(query_word)
    nav.find_element_by_xpath('//*[@id="submit"]').click()
    time.sleep(1)
    ipa_word_from_site = nav.find_element_by_xpath('//*[@id="npTitle"]').text
    ipa_word = ipa_word_from_site.split('\n')[-1]
    return ipa_word # .encode('utf-8')

# AUDIO
def audio(query):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"}
    url = f'https://www.collinsdictionary.com/dictionary/english-french/{query}'
    nav.get(url)
    link = nav.find_elements_by_class_name('audio_play_button')
    audio_link = link[1].get_attribute('data-src-mp3')
    path = pathScript + '/media/' + query + '.mp3'
    try:
        req = request.Request(audio_link, headers=headers)
        data = request.urlopen(req).read()
        with open(path, 'wb') as f:
            f.write(data)
            f.close()
    except Exception as e:
        print(str(e))
    audio_anki = f'[sound:{query}.mp3]'
    return audio_anki

def dealWithPaths():
    # preparing variables 
    source = str(pathlib.Path().resolve()) + '\simple_images'
    destination = str(pathlib.Path().resolve()) + '\media'
    dirs = os.listdir(source)
    for dir in dirs: # or dirs = pathlib.Path().resolve().iterdir()
        directory = os.path.join(source, dir)
        files = pathlib.Path(directory).iterdir()
        for file in files:
            if file.is_file():
                # rename file
                name_file = file.stem
                new_name = name_file[:-2] + file.suffix
                file.rename(pathlib.Path(directory, new_name))
                # move file
                file_name = os.path.join(directory, new_name)
                shutil.move(file_name, destination)
    # remove directories
    for dir in pathlib.Path(source).iterdir():
        try:
            os.rmdir(dir)
            print("Directory '% s' has been removed successfully" % directory)
        except OSError as error:
            print(error)
            print("Directory '% s' can not be removed" % directory)

# CONTA LINHAS ARQUIVO CSV
def count_lines_csv():
    with open(english_words_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        i = 0
        for row in reader:
            i += 1
        csvfile.close()
    return i

# FUNÇÃO QUE ESCREVE QUERY NO FILE
def write_file(query):
    with open(anki_words_file, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(query)
        csvfile.close()

# PROGRESS BAR
def progress_bar(n, n0):
    escala = 2
    porcentagem = int(((n) / n0) * 100)
    print('|' + '\u25A0' * int(porcentagem/escala) + '\u25A1' * int((100 - porcentagem)/escala) + '|', f'[ {porcentagem}% ]')

def read_file():
    query = []
    len_csv = count_lines_csv()
    with open(english_words_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for row in reader:
            for word in row:
                query.append(word)
                query.append(translate_word(word)) # pegar de word_t
                query.append(ipa(query[1])) # selecionar ipa
                query.append(baixarImagem(word)) # baixar imagens
                query.append(audio(word))
                nac = "'[],"
                for i in nac:
                    query[1] = str(query[1]).replace(i, '')
                write_file(query)     
                # progress bar stuff to update the command line in a dynamic way
                if reader.line_num == 1:
                    goback = ''
                else:
                    goback = "\033[F" * 5
                print(f'{goback}\nLines added: {reader.line_num} / {len_csv}\nQuery: {query}')
                progress_bar(reader.line_num, len_csv)
                query.clear()
        csvfile.close()
        print('All the words were translated')

read_file()
dealWithPaths()
nav.quit()