# -*- coding: utf-8 -*-
import random
import string
import vk_api
import time
import json
from auth import token
from vk_api.longpoll import VkLongPoll, VkEventType

#импорт клавиатур
keyboard_0 = open('keyboard_0.json', 'r', encoding='UTF-8').read()
keyboard_1 = open('keyboard_1.json', 'r', encoding='UTF-8').read()
keyboard_2 = open('keyboard_2.json', 'r', encoding='UTF-8').read()

#Генерация рандомного id (требование вк)
def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])

#функция добавления id пользователя в список
def wrt(row, klass):
    users = []
    f = open('users_'+klass+'.txt', 'r')
    for line in f:
        users.append(int(''.join(line)))
    f.close()
    if int(row) in users:
        print('Совпадение')
    else:
        f = open('users_'+klass+'.txt', 'a')
        f.write(row+'\n')
        f.close()

#функция удаления id пользователя из всех списков
def dlt(row):
    users1 = []
    users2 = []
    users3 = []
    users4 = []
    f = open('users_1.txt', 'r')
    users1 = f.readlines()
    f.close()
    f = open('users_2.txt', 'r')
    users2 = f.readlines()
    f.close()
    f = open('users_3.txt', 'r')
    users3 = f.readlines()
    f.close()
    f = open('users_4.txt', 'r')
    users4 = f.readlines()
    f.close()
    f = open('users_1.txt', 'w')
    for line in users1:
        if line != row+"\n":
            f.write(line)
    f.close()
    f = open('users_2.txt', 'w')
    for line in users2:
        if line != row+"\n":
            f.write(line)
    f.close()
    f = open('users_3.txt', 'w')
    for line in users3:
        if line != row+"\n":
            f.write(line)
    f.close()
    f = open('users_4.txt', 'w')
    for line in users4:
        if line != row+"\n":
            f.write(line)
    f.close()

#Функция отправки сообщения
def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': get_random_id()})

#функция отправки сообщения и клавиатуры
def write_msg_kb(user_id, message, keyboard):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': get_random_id(),
                                'keyboard': keyboard})

#ФУНКЦИЯ ОТПРАВКИ ФОТО
def write_photo(user_id, attachment):
    vk.method('messages.send', {'user_id': user_id, 'attachment': attachment, 'random_id': get_random_id()})

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)
translator = str.maketrans('', '', string.punctuation)#удаляем знаки препинания

print('Бот запущен')

calls1 = ['Уведомления включены! За минуту до звонка вы получите от меня сообщение, убедитесь что у вас включены push-уведомления)']
calls2 = ['Если захотите отписаться, наберите "Хочу отписаться"']

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня (то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text
            request = request.translate(translator).lower()#перевод сообщения в нижний регистр и удаление знаков препинания

            # логика ответа
            if 'начать' in request or 'start' in request:
                write_msg_kb(event.user_id, 'Желаете подписаться на уведомления о звонках?', keyboard_1)
            elif 'хочу подписаться' in request:
                write_msg_kb(event.user_id, 'Укажите из какого вы класса:', keyboard_2)
            elif 'отмена' in request:
                write_msg_kb(event.user_id, ':-(', keyboard_0)
            elif 'хочу отписаться' in request:
                dlt(str(event.user_id))
                write_msg_kb(event.user_id, 'Вы отписались от уведомлений!', keyboard_0)


            elif '5 или 8' in request:
                wrt(str(event.user_id), '1') #если 5 или 8 класс, то сохраняем id в users1
                write_msg_kb(event.user_id, calls1, keyboard_0)
                write_msg(event.user_id, calls2)
            elif '6 или 10' in request:
                wrt(str(event.user_id), '2') #если 6 или 10 класс, то сохраняем id в users2
                write_msg_kb(event.user_id, calls1, keyboard_0)
                write_msg(event.user_id, calls2)
            elif '7 или 11' in request:
                wrt(str(event.user_id), '3') #если 7 или 11 класс, то сохраняем id в users3
                write_msg_kb(event.user_id, calls1, keyboard_0)
                write_msg(event.user_id, calls2)
            elif '9 класс' in request:
                wrt(str(event.user_id), '4') #если 9 класс, то сохраняем id в users4
                write_msg_kb(event.user_id, calls1, keyboard_0)
                write_msg(event.user_id, calls2)
            else:
                write_msg(event.user_id, 'Не понимаю вас, наберите "Начать" чтобы вызвать меню.')#если сообщение не связано с подпиской
