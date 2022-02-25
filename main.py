from random import choice

import telebot

token = '5181869878:AAEJvx_0qNkXOdVk0Og-BpNIUwCv-hAEWzY'

bot = telebot.TeleBot(token)

RANDOM_TASKS = [
    'Написать Васе письмо', 'Выучить Python', 'Записаться на курс в Нетологию',
    'Посмотреть 4 сезон Игры престолов'
]

todos = dict()

HELP = '''
Список доступных команд:
* print  - напечать все задачи на заданную дату
* todo - добавить задачу
* random - добавить на сегодня случайную задачу
* help - Напечатать help
'''


def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = [task]


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня')


@bot.message_handler(commands=['add'])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    if len(tail) < 4:
        text = 'Задача не может содержать меньее 3-х символов'
    else:
        task = ' '.join([tail])
        add_todo(date, task)
        text = f'Задача {task} добавлена на дату {date}'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['show'])
def print_(message):
    if message.text.strip() == '/show':
      tasks = 'Введите дату'
    else:
      date = message.text.split()[1].lower()
      if date in todos:
          tasks = ''
          for task in todos[date]:
              tasks += f'[ ] {task}\n'
      else:
          tasks = 'Такой даты нет'
    bot.send_message(message.chat.id, tasks)


bot.polling(none_stop=True)
