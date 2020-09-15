# -*- coding: utf-8 -*-
import random
import string
import vk_api
import time
import schedule

from auth import token
from vk_api.longpoll import VkLongPoll, VkEventType

#Генерация рандомного id (требование вк)
def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])

#Функция для отправки сообщений
def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': get_random_id()})

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)
translator = str.maketrans('', '', string.punctuation) #удаляем знаки препинания

#Варианты уведомлений о звонке
calls = ['Звенит звонок, пора на урок!', 'Урок начинается!', 'А вот и звонок!', 'Звонок', 'Дзинь!' , '&#128276;', '&#128227; Вперёд! К знаниям!']

print('Бот запущен')

#отправка сообщений пользователям из списка users1
def job1():
    users1 = []
    f = open('users_1.txt', 'r')
    for line in f:
        users1.append(int(''.join(line)))
    f.close()
    for id in users1:
        try:
            write_msg(id, random.choice(calls))
        except vk_api.ApiError as err:
            print("Error", err, end="\n"*2)

#отправка сообщений пользователям из списка users2
def job2():
    users2 = []
    f = open('users_2.txt', 'r')
    for line in f:
        users2.append(int(''.join(line)))
    f.close()
    for id in users2:
        try:
            write_msg(id, random.choice(calls))
        except vk_api.ApiError as err:
            print("Error", err, end="\n"*2)

#отправка сообщений пользователям из списка users3
def job3():
    users3 = []
    f = open('users_3.txt', 'r')
    for line in f:
        users3.append(int(''.join(line)))
    f.close()
    for id in users3:
        try:
            write_msg(id, random.choice(calls))
        except vk_api.ApiError as err:
            print("Error", err, end="\n"*2)

#отправка сообщений пользователям из списка users4
def job4():
    users4 = []
    f = open('users_4.txt', 'r')
    for line in f:
        users4.append(int(''.join(line)))
    f.close()
    for id in users4:
        try:
            write_msg(id, random.choice(calls))
        except vk_api.ApiError as err:
            print("Error", err, end="\n"*2)

#назначение задач по времени и дням недели
time1 = ["08:14", "09:14", "10:19", "11:19", "12:19", "13:19", "14:19"] # 5 или 8 класс
time2 = ["09:14", "10:19", "11:19", "12:19", "13:19", "14:19", "15:14"] # 6 или 10 класс
time3 = ["08:29", "09:29", "10:34", "11:29", "12:29", "13:29", "14:29"] # 7 или 11 класс
time4 = ["09:29", "10:34", "11:29", "12:29", "13:29", "14:29", "15:24"] # 9 класс
for time in time1:
    schedule.every().monday.at(time).do(job1)
    schedule.every().tuesday.at(time).do(job1)
    schedule.every().wednesday.at(time).do(job1)
    schedule.every().thursday.at(time).do(job1)
    schedule.every().friday.at(time).do(job1)

for time in time2:
    schedule.every().monday.at(time).do(job2)
    schedule.every().tuesday.at(time).do(job2)
    schedule.every().wednesday.at(time).do(job2)
    schedule.every().thursday.at(time).do(job2)
    schedule.every().friday.at(time).do(job2)

for time in time3:
    schedule.every().monday.at(time).do(job3)
    schedule.every().tuesday.at(time).do(job3)
    schedule.every().wednesday.at(time).do(job3)
    schedule.every().thursday.at(time).do(job3)
    schedule.every().friday.at(time).do(job3)

for time in time4:
    schedule.every().monday.at(time).do(job4)
    schedule.every().tuesday.at(time).do(job4)
    schedule.every().wednesday.at(time).do(job4)
    schedule.every().thursday.at(time).do(job4)
    schedule.every().friday.at(time).do(job4)

while True:
    schedule.run_pending()
