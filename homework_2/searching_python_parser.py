import vk
import json
import random
import os.path

import config

token = config.vk_token
vk_api = vk.API(access_token=token, v=5)


def make_a_dict(new_post):
    new_post_dict = dict()
    new_post_dict['link'] = get_link(new_post)
    new_post_dict['preview'] = up_to_second_sentence(new_post)
    return new_post_dict


def get_link(post):
    return 'https://vk.com/wall%s_%s' % (post['owner_id'], post['id'])


def up_to_second_sentence(new_post):
    up_to_second = min(find_up_to_two_sentences(new_post, '.'), find_up_to_two_sentences(new_post, '\n'))
    return new_post['text'][:up_to_second]


def find_up_to_two_sentences(new_post, symbol):
    first_symbol = new_post['text'].find(symbol)
    second_symbol = new_post['text'].find(symbol, first_symbol + 1)
    if first_symbol != -1 and second_symbol != -1:
        return second_symbol
    else:
        return len(new_post['text'])


def add_json(new_post):
    new_post = make_a_dict(new_post)
    if os.path.isfile('posts.json'):
        posts = json.load(open('posts.json', encoding='utf-8'))
        if all(post['link'] != new_post['link'] and (post['preview'] == 0 or post['preview'] != new_post['preview']) for
               post in posts):
            posts.append(new_post)
    else:
        posts = [new_post]
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, indent=2, ensure_ascii=False)
    return posts


def main():
    new_posts = (vk_api.newsfeed.search(q='программирование Python', count=5))['items']
    for new_post in new_posts:
        posts=add_json(new_post)
    return posts[int(random.uniform(0, len(posts)))]


if __name__ == '__main__':
    main()
