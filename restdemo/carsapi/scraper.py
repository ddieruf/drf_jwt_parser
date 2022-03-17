import requests
import json

def scraper(name='', size=100,page=0,start=0):
    REQ_URL = 'https://www.copart.com/public/lots/search-results'

    headers = {
    'accept' : '*/*',
    'content-type' : 'application/json',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }

    body = {
        'backUrl': "",
        'defaultSort': False,
        'displayName': "",
        'filter': {},
        'freeFormSearch': True,
        'hideImages': False,
        'includeTagByField': {},
        'page': page,
        'query': [name],
        'rawParams': {},
        'searchName': "",
        'size': size,
        'sort': None,
        'specificRowProvided': False,
        'start': start,
        'watchListOnly': False,
    }

    def exclude_other_keys(obj, keys):
        data = {k:v for (k,v) in obj.items() if k in keys}
        data['ln'] = f'https://www.copart.com/lot/{data["ln"]}'
        return data

    

    r = requests.post(REQ_URL, headers=headers, data=json.dumps(body))
    r_json = r.json()['data']['results']['content']
    data = []
    for i in r_json:
        data.append(exclude_other_keys(i, ['ld','ln', 'la']))

    return data


if '__name__' == '__main__':
    pass
