# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

try:
    word_1 = b'attribute'
    word_2 = b'класс' # невозможно записать в байтовом типе
    word_3 = b'функция' # невозможно записать в байтовом типе
    word_4 = b'type'
except SyntaxError as e:
    print(e)
except ValueError as e:
    print(e)
