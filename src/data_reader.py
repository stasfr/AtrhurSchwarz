import csv
import json
from datetime import datetime


def get_result(file_format, is_header, file_path):
    result = {}
    time = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
    
    for row in get_data_csv(file_path, is_header):
        sum = 0
        result[row[0]] = {}
        test_keys = open_keys_file()

        for category in test_keys.keys():
            result[row[0]][category] = {
                'Обзор ценностей': 0,
                'Профиль личности': 0
            }

            values_list = list(test_keys[category]['Обзор ценностей'].split(','))
            person_list = list(test_keys[category]['Профиль личности'].split(','))
            
            for i in values_list:
                sum += int(row[int(i)])
            result[row[0]][category]['Обзор ценностей'] = round(sum/len(values_list), 2)
            sum = 0

            for i in person_list:
                sum += int(row[int(i)+57])
            result[row[0]][category]['Профиль личности'] = round(sum/len(person_list), 2)

    

    with open(f'results\\result_{time}.json', 'w', encoding='utf-8') as result_file:
        json.dump(result, result_file, indent=4, ensure_ascii=False)


def get_data_csv(file_path, is_header):
    with open(file_path, newline='', encoding='utf-8') as data_file:
        readed_file = list(csv.reader(data_file))
        if is_header:
            readed_file.pop(0)
        return readed_file


def open_keys_file():
    with open('data\\keys.json', 'r', encoding='utf-8') as keys_file:
        return json.load(keys_file)


def convert_to_csv(json_result):
    pass


def convert_to_xlsx(json_result):
    pass


def save_result_file(result, file_format):
    pass
