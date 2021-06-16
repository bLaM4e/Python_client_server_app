import json


def write_order_to_json(item, quantity, price, buyer, date):
    data = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }

    with open('orders.json') as f_read:
        file_reader = json.load(f_read)

    file_reader['orders'].append(data)

    with open('orders.json', 'w', encoding='utf-8') as f_append:
        json.dump(file_reader, f_append, indent=4)


write_order_to_json('glass', '30', '150', 'Dmitry', '16.06.2021')
