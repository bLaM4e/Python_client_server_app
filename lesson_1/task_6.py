# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

with open('test_file.txt', 'w') as f:
    f.writelines(['сетевое программирование\n', 'сокет\n', 'декоратор\n'])
    print(f'Создаем файл. Кодировка файла по умолчанию - {f.encoding}\n')

with open('test_file.txt', 'r') as f:
    print(f'Читаем файл с кодировкой по умолчанию:\n{f.read()}')

with open('test_file.txt', 'r', encoding='utf-8') as f:
    try:
        content = f.read()
    except UnicodeDecodeError as e:
        print(f'Пытаемся прочитать файл в формате Unicode и возникает ошибка - {e}')
