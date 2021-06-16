import csv
import re


def get_data(lst):
    main_data = []
    data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    os_prod, os_name, os_code, os_type = data
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    for file in lst:
        with open(file) as f:
            content = f.read().encode('utf-8').decode('utf-8').splitlines()
            for row in content:
                if_prod = re.search(os_prod, row)
                if_name = re.search(os_name, row)
                if_code = re.search(os_code, row)
                if_type = re.search(os_type, row)
                if if_prod:
                    parser(row, os_prod_list, data[0])
                elif if_name:
                    parser(row, os_name_list, data[1])
                elif if_code:
                    parser(row, os_code_list, data[2])
                elif if_type:
                    parser(row, os_type_list, data[3])

    main_data.append(data)
    for line in zip(os_prod_list, os_name_list, os_code_list, os_type_list):
        main_data.append(line)

    return main_data


def parser(row, lst, pattern):
    lst.append(''.join(re.split(pattern, row)).lstrip(':').strip())


def write_to_csv(csv_file, *args):
    data = get_data(args)
    with open(csv_file, 'w', encoding='utf-8') as f:
        f_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        f_writer.writerows(data)


write_to_csv('task_1_file.csv', 'info_1.txt', 'info_2.txt', 'info_3.txt')
