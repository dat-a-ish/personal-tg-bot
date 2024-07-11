from telebot import types
from ..db_utils.load import load_objects, merge_objects
from ..db_configurations.metadata_tables import Request, User
import datetime
import uuid


def send_menu(bot, options_list, message, title):
    if 'Home Menu' not in options_list:
        options_list.append('Home Menu')
    # options_list = list(set(options_list))
    markup = types.InlineKeyboardMarkup(row_width=2)
    for option in options_list:
        markup.add(
            types.InlineKeyboardButton(option,
                                       callback_data=option
                                       .lower()
                                       .replace(' ', '_')))
    bot.send_message(message.chat.id, title, reply_markup=markup)


def log_requests(message_timestamp, username, firstname, lastname, command):
    id = username
    user = User(id=id,
                firstname=firstname,
                lastname=lastname)
    merge_objects(user)
    message_request = Request(id=uuid.uuid4().hex,
                              message_timestamp=datetime.datetime
                              .fromtimestamp(message_timestamp),
                              command=command,
                              username=username)
    load_objects([message_request])
