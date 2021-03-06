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


def make_a_film_base(number_of_films, api_key, method):
    film_base = []
    film_number = 0
    films_in_base = 0

    first_method = method[0]
    other_methods = method[1:]

    while films_in_base < number_of_films:
        film_number += 1
        try:
            film_base.append(make_tmdb_api_request(method=first_method.format(film_number), api_key=api_key))
            for method in other_methods:
                film_base[films_in_base].update(make_tmdb_api_request(method=method.format(film_number), api_key=api_key))
            films_in_base += 1
        except urllib.request.HTTPError:
            pass
    return film_base


my_api_key = os.environ.get('API')

my_base = make_a_film_base(number_of_films=1000, api_key=my_api_key, method=["/movie/{0}", "/movie/{0}/keywords"])

json.dump(my_base, open("my_base.json", "w"))
