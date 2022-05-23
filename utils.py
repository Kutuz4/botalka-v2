from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def form_inline_keyboard(name, buttons_info):
    keyboard = InlineKeyboardMarkup()
    for i in range(len(buttons_info)):
        keyboard.row(InlineKeyboardButton(buttons_info[i], callback_data=name + '_' + buttons_info[i]))
    return keyboard


class States(StatesGroup):
    MEETING = State()
    NAME = State()
    FORM = State()
    SUBJECT = State()
    LEVEL = State()
    ADRESS = State()
    ANKETA = State()
    CHECK = State()
    WORKING = State()


SENDS = {'start': 'Привет! Я боталка 2.0, помогаю людям найти себе соратников для борьбы с прокрастинацией или просто '
                  'хороших друзей. Приступим к знакомству?',
         'name': 'Как тебя зовут?',
         'form': 'Сколько тебе лет?',
         'subject': 'Какой предмет тебя интересует?',
         'level': 'Ты хочешь подтянуть что-то западающее, подготовиться к экзаменам или олимпиадам?',
         'adress': 'Напиши мне свой адрес в формате: номер дома, корпус(если есть), улица, город. \nПример: 6, '
                   'корпус 2, улица Маршала Жукова, Москва',
         'anketa': 'Расскажи немного о себе!',
         'ok?': 'Посмотри, это твоя анкета. Перейдем к работе или хочешь что-то исправить?',
         'ready': 'Напиши мне что угодно, чтобы приступить к поиску',
         'error': 'Ой, случилась какая-то ошибка'}


meeting_kb = form_inline_keyboard('meeting', ['Да', 'Нет'])
yes_button = InlineKeyboardButton('Да', callback_data='work_yes')
no_button = InlineKeyboardButton('Нет', callback_data='work_no')
refresh_anketa = InlineKeyboardButton('Хочу заполнить анкету заново', callback_data='work_new_anketa')
working_keyboard = InlineKeyboardMarkup().row(yes_button).row(no_button).row(refresh_anketa)
subjects_keyboard = form_inline_keyboard('subject', ['Математика', 'Русский язык', 'Физика', 'Информатика', 'Литература', 'Биология', 'Химия', 'География'])
level_keyboard = form_inline_keyboard('level', ['Подтянуть', 'ОГЭ/ЕГЭ/Вступительные', 'Олимпиады'])
ok_keyboard = form_inline_keyboard('ok', ['Перейти к поиску', 'Заполнить анкету заново'])
subjects_dict = {0:'Математика', 1:'Русский язык', 2:'Физика', 3:'Информатика', 4:'Литература', 5:'Биология', 6:'Химия', 7:'География'}
levels_dict = {0:'Подтянуть', 1:'ОГЭ/ЕГЭ/Вступительные', 2:'Олимпиады'}