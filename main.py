# -*- coding: utf-8 -*-
import telebot
from bot.sentence_maker import SentenceMaker
from bot.utils import ConfigParser


cfg = ConfigParser('config.yml')
bot = telebot.TeleBot(cfg.token)


@bot.message_handler(commands=['start'])
def init_reply(message):
    kbord = telebot.types.InlineKeyboardMarkup()
    kbord.add(telebot.types.InlineKeyboardButton(text='Да', callback_data='text'))
    bot.send_message(message.chat.id, text='Сгенерировать заголовок?', reply_markup=kbord)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    sent = sm.make_any_sentence()
    kbord = telebot.types.InlineKeyboardMarkup()
    kbord.add(telebot.types.InlineKeyboardButton(text='Ещё один!', callback_data='text'))
    bot.send_message(call.message.chat.id, text=sent, reply_markup=kbord)


if __name__ == '__main__':
    sm = SentenceMaker(cfg.model_fp)
    bot.infinity_polling()
