import urllib.request
import urllib.parse
import json
import os


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

my_api_key = os.environ['API']

print("Enter the movie's number")
number = int(input())
print(make_tmdb_api_request(method="/movie/{0}".format(number), api_key=my_api_key)['budget'])

# The Saw 2's number is 215
