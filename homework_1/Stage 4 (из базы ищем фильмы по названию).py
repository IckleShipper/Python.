import urllib.request
import urllib.parse
import json


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)


my_api_key = 'fbb77ca50be1bbc7f66bd025447db05a'

my_list = json.load(open('my_base.json', 'r'))

print('Enter the word')
search = input()

for film in my_list:
    if film['original_title'].find(search) !=-1:
        print(film['original_title'])
