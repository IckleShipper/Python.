# -*- coding: utf-8 -*-

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random

import searching_python_parser
import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
message_number = 0
words = ['Яхта', 'Парус', 'одни', 'Ялта', 'Август', 'тобою']


def check_word(text):
    global words
    for word in words:
        if text.find(word) != -1:
            return ['Парус', 'В этом мире только мы одни~', 'Ялта', 'Август', 'И мы с тобою влюблены~', 'Мяу'][
                words.index(word)]
    lyrics = random.choice(['Яхта', 'Парус', 'Ялта', 'Август'])
    print('-I sang "%s"' % lyrics)
    return lyrics


def notification(update):
    global message_number
    message_number += 1
    if update['message']['chat']['type'] == 'private':
        print('%s. New message "%s" from username: %s, name: %s, at %s!!' % (message_number,
                                                                             update['message']['text'],
                                                                             update['message']['chat']['username'],
                                                                             update['message']['chat']['first_name'],
                                                                             update['message']['date']))
    else:
        print('%s. New message "%s" from group "%s", at %s!!' % (message_number,
                                                                 update['message']['text'],
                                                                 update['message']['chat']['title'],
                                                                 update['message']['date']))


def start_command(bot, update):
    notification(update)
    update.message.reply_text('Привет, девчонки. Я Юрка\n/help?')


def help_command(bot, update):
    notification(update)
    update.message.reply_text('Все, что я умею - это:\n/start, /help, /pynews и петь')


def spam(bot, update):
    notification(update)
    update.message.reply_text(check_word(update['message']['text']))


def error(bot, update, error):
    notification(update)
    logging.warning('Update "%s" caused error "%s"', update, error)


def pynews_command(bot, update):
    notification(update)
    sent_post = searching_python_parser.main()
    update.message.reply_text('%s\n%s' % (sent_post['link'], sent_post['preview']))
    print('-I sent a post %s: %s' % (sent_post['link'], sent_post['preview']))


def main():
    updater = Updater(token=config.telegram_bot_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(CommandHandler('pynews', pynews_command))
    dispatcher.add_handler(MessageHandler(Filters.all, spam))
    dispatcher.add_error_handler(error)

    updater.start_polling()


if __name__ == '__main__':
    main()
