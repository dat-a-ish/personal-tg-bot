from .helper import send_menu
import boto3
from .config import mobile_phone, first_name, last_name, \
    linkedin_link, whats_app_link, email, github_link


def send_welcome_base(bot, message):
    title = f'''
            Hi!
My name is {first_name} {last_name} and this is my personal Telegram Bot.
            '''
    options = ['Get CV',
               'Contact Real Egor',
               # 'See Skills',
               'See Projects']
    send_menu(bot, options, message, title)


def home_menu(bot, message):
    send_welcome_base(bot, message)


def contact_real_egor(bot, message):
    whats_app_text = f"""<b>Contact Egor</b>:
- <a href='{linkedin_link}'>Egor's LinkedIn</a>
- <a href='{github_link}'>Egor's GitHub</a>
- <a href='{whats_app_link}'>Egor's WhatsApp</a>
- Egor's Email: <b>{email}</b>"""
    bot.send_message(message.chat.id, whats_app_text,
                     parse_mode='HTML')
    bot.send_contact(message.chat.id, phone_number=mobile_phone,
                     first_name=first_name, last_name=last_name)
    send_menu(bot, [], message, 'Home Page:')


def get_cv(bot, message):
    warning_text = 'Sending a file. It might take a couple of seconds'
    bot.send_message(message.chat.id, warning_text)
    s3 = boto3.client('s3')
    file_name = 'CV.docx'
    s3.download_file('egor-personal-data', file_name, file_name)
    with open(file_name, 'rb') as cv_f:
        cv = cv_f.read()
        bot.send_document(message.chat.id, cv, visible_file_name=file_name)
    send_menu(bot, [], message, 'Home Page:')


def see_projects(bot, message):
    bot.send_message(message.chat.id,
                     '''This function still isn\'t implemented.
Sorry. It will be ready soon.''')
    send_menu(bot, [], message, 'Home Page:')
