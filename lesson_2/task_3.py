import yaml


def write_to_yaml(file, data):
    with open(file, 'w', encoding='utf-8') as f_yaml:
        yaml.dump(data, f_yaml, allow_unicode=True)


def read_from_yaml(file):
    with open(file, 'r', encoding='utf-8') as f_yaml:
        return yaml.load(f_yaml, Loader=yaml.FullLoader)


data_dict = {
    'key1': [10, 'string', bool],
    'key2': 100,
    'key3': {
        'key1': '5€',
        'key2': '6€',
        'key3': '7€',
    }
}

write_to_yaml('file.yaml', data_dict)
data_read = read_from_yaml('file.yaml')
print(f'Считанные данные из созданного файла совпадают с исходными? {data_read == data_dict}')
