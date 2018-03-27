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


def input_film():
    film_id = 0
    while film_id == 0:
        print("Enter the film's original title")
        title = input()

        for film in my_list:
            if film['original_title'] == title:
                film_id = film['id']
                keywords = {keyword_dict['name'] for keyword_dict in film['keywords']}
                words_in_title = set(title.split())
                significant_words = set()
                for word in words_in_title:
                    if len(word) > 3:
                        significant_words.add(word)
                break
    return title, film_id, keywords, significant_words


def questions():
    keywords_number = -1
    while keywords_number < 0 or keywords_number % 1 != 0:
        print("How many common keywords do you want? (at least)")
        try:
            keywords_number = float(input())
        except ValueError:
            pass

    answer = 0
    while answer not in ['N', 'Y']:
        print("Do you want movies with similar titles? Y/N")
        answer = input()
    return keywords_number, answer


my_api_key = os.environ['API']
my_list = json.load(open('my_base.json', 'r'))

my_title, my_film_id, my_keywords, my_significant_words = input_film()

keywords_number, answer = questions()
recommendation_list = []
for film in my_list:
    if film['id'] != my_film_id:
        current_keywords = {keyword_dict['name'] for keyword_dict in film['keywords']}
        if len(my_keywords & current_keywords) >= keywords_number:
            recommendation_list.append(film['original_title'])
        elif answer == "Y":
            for word in my_significant_words:
                if film['original_title'].find(word) != -1:
                    recommendation_list.append(film['original_title'])
                    break
for original_title in sorted(recommendation_list):
    print(original_title)
# Easy to check on Dirty Harry
