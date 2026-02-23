import random
import json
import sys
from textwrap import dedent


def load_bible_file(file='index.json'):
    '''Tenta abrir o index.json'''
    try:
        with open(file, 'r', encoding='utf-8') as f_obj:
            bible = json.load(f_obj)

    except FileNotFoundError:
        print(f'O arquivo "{file}" não foi encontrado!')
        print('Caso o arquivo tenha sido renomeado, informe'
              ' à função "load_bible_file()".')
        sys.exit(1)
    return bible


def random_verse(bible):
    '''Gera o verso usando um objeto que carrega o arquivo'''
    book = random.choice(bible)
    chapters = book['chapters']

    chapter = random.choice(list(chapters.keys()))

    verse = random.randint(1, book['chapters'][chapter])

    book_name = book['name']
    return (book, book_name, chapter, verse)


def main_loop():

    bible = load_bible_file()  # Abre apenas uma vez!

    while True:
        try:
            answer = input(
                'Deseja gerar um verso aleatório? [S/n]').strip().lower()

        except KeyboardInterrupt:
            break

        if answer == 'n':
            break

        else:
            print('Gerando...')

            book, name, chapter, verse = random_verse(bible=bible)

            message = dedent(f"""   
            ===================================               
            =Aqui está uma sugestão sorteada: =
            ===================================
             -------------------------------
             Nome do livro: {name}
             Capitulo Sorteado: {chapter}
             Verso sorteado: {verse}
             Autor: {book['author']}
             -------------------------------
             """)

            print(message)

    print('\nVocê saiu.')
