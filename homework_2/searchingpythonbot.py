# -*- coding: utf-8 -*-

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random

import searchingpythonparser
import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
message_number = 0


def notification(update):
    global message_number
    message_number += 1
    print('%s. New message "%s" from username: %s, name: %s, at %s!!' % (message_number,
                                                                         update['message']['text'],
                                                                         update['message']['chat']['username'],
                                                                         update['message']['chat']['first_name'],
                                                                         update['message']['date']))


def start_command(bot, update):
    notification(update)
    update.message.reply_text('Привет, девчонки. Я Юрка\n/help?')


def help_command(bot, update):
    notification(update)
    update.message.reply_text('Все, что я умею - это:\n/start, /help, /pynews и петь')


def spam(bot, update):
    notification(update)
    lyrics = random.choice(['Яхта', 'Парус', 'Ялта', 'Август'])
    update.message.reply_text(lyrics)
    print('-I sang "%s"' % lyrics)


def error(bot, update, error):
    notification(update)
    logging.warning('Update "%s" caused error "%s"', update, error)


def pynews_command(bot, update):
    notification(update)
    sent_post = searchingpythonparser.main()
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
