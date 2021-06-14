# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
# из байтовового в строковый тип на кириллице.

import subprocess

args_1 = ['ping', 'ya.ru']
args_2 = ['ping', 'youtube.com']

subproc_ping_1 = subprocess.Popen(args_1, stdout=subprocess.PIPE)
for line in subproc_ping_1.stdout:
    line = line.decode('cp866').encode('utf-8') # c переформатированеим в utf-8
    print(line.decode('utf-8'), end='')

subproc_ping_2 = subprocess.Popen(args_2, stdout=subprocess.PIPE)
for line in subproc_ping_2.stdout:
    line = line.decode('cp866') # без переформатирования в utf-8
    print(line, end='')
