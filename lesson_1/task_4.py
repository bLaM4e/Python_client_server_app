# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

word_1, word_2, word_3, word_4 = 'разработка', 'администрирование', 'protocol', 'standard'

word_1b = word_1.encode('utf-8')
word_2b = word_2.encode('utf-8')
word_3b = word_3.encode('utf-8')
word_4b = word_4.encode('utf-8')
print(word_1b)
print(word_2b)
print(word_3b)
print(word_4b)

word_1 = word_1b.decode('utf-8')
word_2 = word_2b.decode('utf-8')
word_3 = word_3b.decode('utf-8')
word_4 = word_4b.decode('utf-8')
print(word_1)
print(word_2)
print(word_3)
print(word_4)
