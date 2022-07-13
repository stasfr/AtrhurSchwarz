from bs4 import BeautifulSoup
import json


def get_keys():
    with open('get_keys\\index.html', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    all_tr = soup.find_all('tr')
    keys = {}
    
    for tr in all_tr:
        list_p = tr.find_all('p')

        keys[list_p[0].text] = {
            'value': list_p[1].text,
            'profile': list_p[2].text
        } 
    
    with open('keys.json', 'w', encoding='utf-8') as keys_file:
        json.dump(keys, keys_file, indent=4, ensure_ascii=False)

get_keys()
