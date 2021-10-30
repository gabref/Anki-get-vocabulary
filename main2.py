import csv
import random
import time

sequencia_palavras = [['chienne','chien'],'garçon',['chatte','chat'], 'gateaux',' eau','noeuf','oeuf']
palavra_ipa = 'shiên'
english_words_file = r'D:\memor\Documents\Programming\Python\Projetos\Anki_Vocabulary\English_Words.csv'
anki_words_file = r'D:\memor\Documents\Programming\Python\Projetos\Anki_Vocabulary\Anki_Words.csv'

def translate_word(query):
    word_t = random.choice(query)
    return word_t

def ipa():
    return palavra_ipa

def imagem(query):
    return str(query) + '.jpeg'

def audio(query):
    return str(query) + '.mp3'

def count_lines_csv():
    with open(english_words_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        i = 0
        for row in reader:
            i += 1
        csvfile.close()
    return i

def read_file():
    query = []
    len_csv = count_lines_csv()
    with open(english_words_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for row in reader:
            for word in row:
                query.append(word)
                query.append(translate_word(sequencia_palavras)) # pegar de word_t
                query.append(ipa()) # selecionar ipa
                query.append(imagem(word))
                query.append(audio(word))
                write_file(query)     
                # progress bar stuff
                if reader.line_num == 1:
                    goback = ''
                else:
                    goback = "\033[F" * 4
                print(f'{goback}\nLines added: {reader.line_num} / {len_csv}\nQuery: {query}')
                progress_bar(reader.line_num, len_csv)
                query.clear()
                time.sleep(0.5)
        csvfile.close()
        print('All the words were translated')

def write_file(query):
    with open(anki_words_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(query)
        csvfile.close()

def progress_bar(n, n0):
    escala = 2
    porcentagem = int(((n) / n0) * 100)
    print('|' + '\u25A0' * int(porcentagem/escala) + '\u25A1' * int((100 - porcentagem)/escala) + '|', f'[ {porcentagem}% ]')

read_file()