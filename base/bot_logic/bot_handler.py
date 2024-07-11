import telebot
from .helper import log_requests
from . import base_functions
from .config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello', 'help'])
def send_welcome(message):
    log_requests(message.date, message.chat.username,
                 message.chat.first_name, message.chat.last_name,
                 send_welcome.__name__)
    base_functions.send_welcome_base(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def handle_menu_answer(callback):
    message = callback.message
    if message:
        log_requests(message.date, message.chat.username,
                     message.chat.first_name, message.chat.last_name,
                     callback.data)
        func = getattr(base_functions, callback.data)
        func(bot, message)


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
