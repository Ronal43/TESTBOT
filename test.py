#coding:utf-8
import telebot, config
from telebot import types
import datetime
from datetime import date
import time
import os
import sys
import subprocess
import string
import re
import random
from collections import Counter


knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts


def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        return 0



def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            date = datetime.date.today()
            print (str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)
            vremya = time.asctime(time.localtime(time.time()))
            print (vremya)
            spisok = [str(vremya) + '-' + str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text]
            filename = str(date) + "_" + m.chat.first_name +'.txt'
            spisok2 = open("/home/makar/rabotayet/Bot_working/logs/" + filename, 'a')
            for index in spisok:
                spisok2.write(index + '\n')
            spisok2.close


bot=telebot.TeleBot(config.TOKEN)
bot.set_update_listener(listener)

def main():

    @bot.message_handler(commands=["start"])
    def handle_text(message): 
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        priv = ('Привет;)', 'Давай работать, что-ли?:Р', 'Хочешь аккаунтов?)', 'Мамбы, вк!! Легко и просто!!!', 'Нажми на кно... Хотя нет, не нажим... Жми, короче, я согласен...Может...', 'Давай нажимать кнопочки и ломать меня))', 'Люблю, когда нажимают кнопочки))', 'Надоели хачики? Попроси картиночку!!')
        #orig_mamba = open('mambaorig.txt', 'r+')
        rab_mamba = open('mamba.txt', 'r+')
        mamba_list = (rab_mamba.read())
        mambalist = mamba_list.split('\n')
        mambishche = [x for x in mambalist if x != '']
        mambaresultat = str(len(mambishche))
        print(mambaresultat)
        #omambalist = (orig_mamba.read())
        #omamba_list = omambalist.split('\n')
        #result = []
        #for index in mambishche:
        #    if index in omamba_list:
        #        result.append(index)
        #print(len(result))
        #mambaresultat = str(len(result))
#############
        #orig_vk = open('vkorig.txt', 'r+')
        rab_vk = open('vk.txt', 'r+')
        vk_list = (rab_vk.read())
        vklist = vk_list.split('\n')
        vk_proverka = [x for x in vklist if x != '']
        vkresultat = str(len(vk_proverka))
        print(vkresultat)
        #ovk_list = (orig_vk.read())
        #ovklist = ovk_list.split('\n')
        #vkresult = []
        #for index in vk_proverka:
        #    if index in ovklist:
        #        vkresult.append(index)
        #print(vkresult)
        #print(len(vkresult))
        #vkresultat = str(len(vkresult))
############
        #orig_mamba_ua = open('mambaorigua.txt', 'r+')
        rab_mamba_ua = open('mambaua.txt', 'r+')
        mamba_list_ua = (rab_mamba_ua.read())
        mambalist_ua = mamba_list_ua.split('\n')
        mambishche_ua = [x for x in mambalist_ua if x != '']
        mambauaresult = str(len(mambishche_ua))
        print(mambauaresult)
        #omambalist_ua = (orig_mamba_ua.read())
        #omamba_list_ua = omambalist_ua.split('\n')
        #mamba_ua_result = []
        #for index in mambishche_ua:
        #    if index in omamba_list_ua:
        #        mamba_ua_result.append(index)
        #print(len(mamba_ua_result))
        #mambauaresult = str(len(mamba_ua_result))
#############
        #orig_vkua = open('vkorigua.txt', 'r+')
        rab_vkua = open('vkkiev.txt', 'r+')
        vk_list_ua = (rab_vkua.read())
        vklist_ua = vk_list_ua.split('\n')
        vk_proverka_ua = [x for x in vklist_ua if x != '']
        vkuaresultat = str(len(vk_proverka_ua))
        print(vkuaresultat)
        #ovk_list_ua = (orig_vkua.read())
        #ovklist_ua = ovk_list_ua.split('\n')
        #vkresult_ua = []
        #for index in vk_proverka_ua:
        #    if index in ovklist_ua:
        #        vkresult_ua.append(index)
        #print(len(vkresult_ua))
        #vkuaresultat = str(len(vkresult_ua))
        user_markup.row('Нужна мамба на Киев') 
        user_markup.row('Получить вк Киев')
        user_markup.row('Получить мамбу МСК') 
        user_markup.row('Получить вк МСК')
        user_markup.row('КНОПКА')
        bot.send_message(message.from_user.id, random.choice(priv), reply_markup=user_markup)
        bot.send_message(message.chat.id, 'У меня есть в наличии много вкусностей:)\n')
        bot.send_message(message.chat.id, 'Mamba.ru: ' + mambaresultat + '\nVk.com: ' + vkresultat + '\nMamba.UA: ' + mambauaresult + '\nvk.com(ua): ' + vkuaresultat)



    @bot.message_handler(func=lambda message: message.text == "КНОПКА")
    def handle_text(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('На главную')
        bot.send_message(message.from_user.id, 'Иди ко мне, сладкая...')
        kartink = random.choice(os.listdir("/home/makar/rabotayet/Bot_working/kartinki/"))
        kartinka = "/home/makar/rabotayet/Bot_working/kartinki/" + kartink
        print (kartink)
        print (kartinka)
        bot.send_photo(message.from_user.id, open(kartinka, 'rb'))
        

    @bot.message_handler(commands=["help"]) 
    def start(message):
        bot.send_message(message.chat.id, '')


    @bot.message_handler(func=lambda message: message.text == "На главную")
    def handle_text(message): 
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        #orig_mamba = open('mambaorig.txt', 'r+')
        rab_mamba = open('mamba.txt', 'r+')
        mamba_list = (rab_mamba.read())
        mambalist = mamba_list.split('\n')
        mambishche = [x for x in mambalist if x != '']
        mambaresultat = str(len(mambishche))
        print(mambaresultat)
        #omambalist = (orig_mamba.read())
        #omamba_list = omambalist.split('\n')
        #result = []
        #for index in mambishche:
        #    if index in omamba_list:
        #        result.append(index)
        #print(len(result))
        #mambaresultat = str(len(result))
#############
        #orig_vk = open('vkorig.txt', 'r+')
        rab_vk = open('vk.txt', 'r+')
        vk_list = (rab_vk.read())
        vklist = vk_list.split('\n')
        vk_proverka = [x for x in vklist if x != '']
        vkresultat = str(len(vk_proverka))
        print(vkresultat)
        #ovk_list = (orig_vk.read())
        #ovklist = ovk_list.split('\n')
        #vkresult = []
        #for index in vk_proverka:
        #    if index in ovklist:
        #        vkresult.append(index)
        #print(vkresult)
        #print(len(vkresult))
        #vkresultat = str(len(vkresult))
############
        #orig_mamba_ua = open('mambaorigua.txt', 'r+')
        rab_mamba_ua = open('mambaua.txt', 'r+')
        mamba_list_ua = (rab_mamba_ua.read())
        mambalist_ua = mamba_list_ua.split('\n')
        mambishche_ua = [x for x in mambalist_ua if x != '']
        mambauaresult = str(len(mambishche_ua))
        print(mambauaresult)
        #omambalist_ua = (orig_mamba_ua.read())
        #omamba_list_ua = omambalist_ua.split('\n')
        #mamba_ua_result = []
        #for index in mambishche_ua:
        #    if index in omamba_list_ua:
        #        mamba_ua_result.append(index)
        #print(len(mamba_ua_result))
        #mambauaresult = str(len(mamba_ua_result))
#############
        #orig_vkua = open('vkorigua.txt', 'r+')
        rab_vkua = open('vkkiev.txt', 'r+')
        vk_list_ua = (rab_vkua.read())
        vklist_ua = vk_list_ua.split('\n')
        vk_proverka_ua = [x for x in vklist_ua if x != '']
        vkuaresultat = str(len(vk_proverka_ua))
        print(vkuaresultat)
        #ovk_list_ua = (orig_vkua.read())
        #ovklist_ua = ovk_list_ua.split('\n')
        #vkresult_ua = []
        #for index in vk_proverka_ua:
        #    if index in ovklist_ua:
        #        vkresult_ua.append(index)
        #print(len(vkresult_ua))
        #vkuaresultat = str(len(vkresult_ua))
        user_markup.row('Нужна мамба на Киев') 
        user_markup.row('Получить вк Киев')
        user_markup.row('Получить мамбу МСК') 
        user_markup.row('Получить вк МСК')
        user_markup.row('КНОПКА')
        glavn = ('Опять мы тут, продолжим же)', 'Что-нибудь еще?', 'Продолжаем.', 'Ну, что еще?','Меня разорили...','Я снова потерял часть себя:(','Желаете еще чего-нибудь?')
        bot.send_message(message.from_user.id, random.choice(glavn), reply_markup=user_markup)
        bot.send_message(message.chat.id, 'Теперь у меня: \n' +'Mamba.ru: ' + mambaresultat + '\nVk.com: ' + vkresultat + '\nMamba.UA: ' + mambauaresult + '\nvk.com(ua): ' + vkuaresultat, reply_markup=user_markup)

	
    @bot.message_handler(func=lambda message: message.text == "Нужна мамба на Киев")
    def handle_text(message):
        #orig_mamba_ua = open('mambaorigua.txt', 'r+')
        rab_mamba_ua = open('mambaua.txt', 'r+')
        mamba_list_ua = (rab_mamba_ua.read())
        mambalist_ua = mamba_list_ua.split('\n')
        mambishche_ua = [x for x in mambalist_ua if x != '']
        mambauaresult = str(len(mambishche_ua))
        print(mambauaresult)
        #omambalist_ua = (orig_mamba_ua.read())
        #omamba_list_ua = omambalist_ua.split('\n')
        #mamba_ua_result = []
        #for index in mambishche_ua:
        #    if index in omamba_list_ua:
        #        mamba_ua_result.append(index)
        #print(len(mamba_ua_result))
        #mambauaresult = str(len(mamba_ua_result))
        if mambauaresult == '1' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Одна мамба')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько нужно? \nОстаток: " + mambauaresult, reply_markup=user_markup)
            @bot.message_handler(func=lambda message: message.text == "Одна мамба")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mambaua, reply_markup=user_markup)
                    bot.send_message(m.chat.id, 'Работай хорошо, тогда у тебя всегда будут свежие и красивые аккаунты;)')
                    print (mambaua)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
        elif mambauaresult == '2' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Одна мамба')
            user_markup.row('Две мамбы')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько нужно? \nОстаток: " + mambauaresult, reply_markup=user_markup)
            @bot.message_handler(func=lambda message: message.text == "Одна мамба")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mambaua, reply_markup=user_markup)
                    bot.send_message(m.chat.id, 'Работай хорошо, тогда у тебя всегда будут свежие и красивые аккаунты;)')
                    print (mambaua)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
            @bot.message_handler(func=lambda message: message.text == "Две мамбы")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua1 = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mambaua)
                    bot.send_message(m.chat.id, mambaua1, reply_markup=user_markup)
                    print (mambaua)
                    print (mambaua1)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
        elif mambauaresult == '3' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Одна мамба')
            user_markup.row('Две мамбы')
            user_markup.row('Три мамбы')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько нужно? \nОстаток: " + mambauaresult, reply_markup=user_markup)
            @bot.message_handler(func=lambda message: message.text == "Одна мамба")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mambaua, reply_markup=user_markup)
                    bot.send_message(m.chat.id, 'Работай хорошо, тогда у тебя всегда будут свежие и красивые аккаунты;)')
                    print (mambaua)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
            @bot.message_handler(func=lambda message: message.text == "Две мамбы")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua1 = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mambaua)
                    bot.send_message(m.chat.id, mambaua1, reply_markup=user_markup)
                    print (mambaua)
                    print (mambaua1)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
            @bot.message_handler(func=lambda message: message.text == "Три мамбы")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua1 = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua2 = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Это уже дело)) \n '+mambaua)
                    bot.send_message(m.chat.id, mambaua1)
                    bot.send_message(m.chat.id, mambaua2, reply_markup=user_markup)
                    print (mambaua)
                    print (mambaua1)
                    print (mambaua2)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
        elif mambauaresult == '4' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Одна мамба')
            user_markup.row('Две мамбы')
            user_markup.row('Три мамбы')
            user_markup.row('Четыре мамбы')   
            user_markup.row('На главную')   
            bot.send_message(message.chat.id, "Сколько нужно? \nОстаток: " + mambauaresult, reply_markup=user_markup)
            @bot.message_handler(func=lambda message: message.text == "Одна мамба")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mambaua, reply_markup=user_markup)
                    bot.send_message(m.chat.id, 'Работай хорошо, тогда у тебя всегда будут свежие и красивые аккаунты;)')
                    print (mambaua)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
            @bot.message_handler(func=lambda message: message.text == "Две мамбы")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua1 = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mambaua)
                    bot.send_message(m.chat.id, mambaua1, reply_markup=user_markup)
                    print (mambaua)
                    print (mambaua1)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
            @bot.message_handler(func=lambda message: message.text == "Три мамбы")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua1 = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua2 = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Это уже дело)) \n '+mambaua)
                    bot.send_message(m.chat.id, mambaua1)
                    bot.send_message(m.chat.id, mambaua2, reply_markup=user_markup)
                    print (mambaua)
                    print (mambaua1)
                    print (mambaua2)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
            @bot.message_handler(func=lambda message: message.text == "Четыре мамбы")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]  
                    mambaua1 = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua2 = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua3 = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Это сильно)) \n '+mambaua)
                    bot.send_message(m.chat.id, mambaua1)
                    bot.send_message(m.chat.id, mambaua2)
                    bot.send_message(m.chat.id, mambaua3, reply_markup=user_markup)
                    print (mambaua)
                    print (mambaua1)
                    print (mambaua2)
                    print (mambaua3)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
        elif mambauaresult == '0' :
            user_markup.row('На главную')   
            bot.send_message(message.chat.id, "Не осталось совсем, реально, ждите, пока закинут. \nАкков: " + mambaresult, reply_markup=user_markup)    
        else :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Одна мамба')
            user_markup.row('Две мамбы')
            user_markup.row('Три мамбы')
            user_markup.row('Четыре мамбы')
            user_markup.row('Пять мамб')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько нужно? \nВ наличии: " + mambauaresult, reply_markup=user_markup)
            @bot.message_handler(func=lambda message: message.text == "Одна мамба")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mambaua, reply_markup=user_markup)
                    bot.send_message(m.chat.id, 'Работай хорошо, тогда у тебя всегда будут свежие и красивые аккаунты;)')
                    print (mambaua)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
            @bot.message_handler(func=lambda message: message.text == "Две мамбы")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua1 = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mambaua)
                    bot.send_message(m.chat.id, mambaua1, reply_markup=user_markup)
                    print (mambaua)
                    print (mambaua1)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
            @bot.message_handler(func=lambda message: message.text == "Три мамбы")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua1 = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua2 = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Это уже дело)) \n '+mambaua)
                    bot.send_message(m.chat.id, mambaua1)
                    bot.send_message(m.chat.id, mambaua2, reply_markup=user_markup)
                    print (mambaua)
                    print (mambaua1)
                    print (mambaua2)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
            @bot.message_handler(func=lambda message: message.text == "Четыре мамбы")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]  
                    mambaua1 = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua2 = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua3 = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Это сильно)) \n '+mambaua)
                    bot.send_message(m.chat.id, mambaua1)
                    bot.send_message(m.chat.id, mambaua2)
                    bot.send_message(m.chat.id, mambaua3, reply_markup=user_markup)
                    print (mambaua)
                    print (mambaua1)
                    print (mambaua2)
                    print (mambaua3)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
            @bot.message_handler(func=lambda message: message.text == "Пять мамб")
            def command_text_hi(m):
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
                    mambaua = uaaccount.pop (0)
                    del uaaccount[0]  
                    mambaua1 = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua2 = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua3 = uaaccount.pop (0)
                    del uaaccount[0]
                    mambaua4 = uaaccount.pop (0)
                    del uaaccount[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Ну, если ты справишься с ними... \n '+mambaua)
                    bot.send_message(m.chat.id, mambaua1)
                    bot.send_message(m.chat.id, mambaua2)
                    bot.send_message(m.chat.id, mambaua3)
                    bot.send_message(m.chat.id, mambaua4, reply_markup=user_markup)
                    print (mambaua)
                    print (mambaua1)
                    print (mambaua2)
                    print (mambaua3)
                    print (mambaua4)
                    print (uaaccount)
                    uamamba = open('mambaua.txt', 'w')
                    for index in uaaccount:
                          uamamba.write(index + '\n')
                    uamamba.close
                    uamamba = open('mambaua.txt', 'r+')
                    uaspisok = (uamamba.read())
                    uaaccount = uaspisok.split('\n')
                    print (uaaccount)
                    uamamba.close()
	
	
    @bot.message_handler(func=lambda message: message.text == "Получить вк Киев") 
    def handle_text(message):
        #orig_vkua = open('vkorigua.txt', 'r+')
        rab_vkua = open('vkkiev.txt', 'r+')
        vk_list_ua = (rab_vkua.read())
        vklist_ua = vk_list_ua.split('\n')
        vk_proverka_ua = [x for x in vklist_ua if x != '']
        vkuaresultat = str(len(vk_proverka_ua))
        print(vkuaresultat)
        #ovk_list_ua = (orig_vkua.read())
        #ovklist_ua = ovk_list_ua.split('\n')
        #vkresult_ua = []
        #for index in vk_proverka_ua:
        #    if index in ovklist_ua:
        #        vkresult_ua.append(index)
        #print(len(vkresult_ua))
        #vkuaresultat = str(len(vkresult_ua))
        if vkuaresultat == '1':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('1 акк')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько? \nОстаток: " + vkuaresultat, reply_markup=user_markup)
            @bot.message_handler(func=lambda message: message.text == '1 акк')
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Лови:) \n' +vkkiev)
                  bot.send_message(m.chat.id, 'Нужно будет еще что-нибудь - приходи.', reply_markup=user_markup)
                  print (vkkiev)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
        elif vkuaresultat == '2' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('1 акк')
            user_markup.row('2 акка')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько? \nОстаток: " + vkuaresultat, reply_markup=user_markup)
            bot.send_message(message.chat.id, "Сколько? \nОстаток: " + vkuaresultat, reply_markup=user_markup)    
            @bot.message_handler(func=lambda message: message.text == '1 акк')
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Лови:) \n' +vkkiev)
                  bot.send_message(m.chat.id, 'Нужно будет еще что-нибудь - приходи.', reply_markup=user_markup)
                  print (vkkiev)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
            @bot.message_handler(func=lambda message: message.text == "2 акка")
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev1 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ну, два так два. Мне не жалко...\n' +vkkiev)
                  bot.send_message(m.chat.id, vkkiev1,reply_markup=user_markup)
                  print (vkkiev+' '+vkkiev1)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
        elif vkuaresultat == '3' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('1 акк')
            user_markup.row('2 акка')
            user_markup.row('3 акка')   
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько? \nОстаток: " + vkuaresultat, reply_markup=user_markup)
            @bot.message_handler(func=lambda message: message.text == '1 акк')
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Лови:) \n' +vkkiev)
                  bot.send_message(m.chat.id, 'Нужно будет еще что-нибудь - приходи.', reply_markup=user_markup)
                  print (vkkiev)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
            @bot.message_handler(func=lambda message: message.text == "2 акка")
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev1 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ну, два так два. Мне не жалко...\n' +vkkiev)
                  bot.send_message(m.chat.id, vkkiev1,reply_markup=user_markup)
                  print (vkkiev+' '+vkkiev1)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
            @bot.message_handler(func=lambda message: message.text == "3 акка")
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev1 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev2 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'О, мастер своего дела?;) \n' +vkkiev)
                  bot.send_message(m.chat.id, vkkiev1)
                  bot.send_message(m.chat.id, vkkiev2, reply_markup=user_markup)
                  print (vkkiev+' '+vkkiev1+' '+vkkiev2)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
        elif vkuaresultat == '4' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('1 акк')
            user_markup.row('2 акка')
            user_markup.row('3 акка')
            user_markup.row('4 акка')   
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько? \nОстаток: " + vkuaresultat, reply_markup=user_markup)
            @bot.message_handler(func=lambda message: message.text == '1 акк')
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Лови:) \n' +vkkiev)
                  bot.send_message(m.chat.id, 'Нужно будет еще что-нибудь - приходи.', reply_markup=user_markup)
                  print (vkkiev)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
            @bot.message_handler(func=lambda message: message.text == "2 акка")
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev1 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ну, два так два. Мне не жалко...\n' +vkkiev)
                  bot.send_message(m.chat.id, vkkiev1,reply_markup=user_markup)
                  print (vkkiev+' '+vkkiev1)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
            @bot.message_handler(func=lambda message: message.text == "3 акка")
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev1 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev2 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'О, мастер своего дела?;) \n' +vkkiev)
                  bot.send_message(m.chat.id, vkkiev1)
                  bot.send_message(m.chat.id, vkkiev2, reply_markup=user_markup)
                  print (vkkiev+' '+vkkiev1+' '+vkkiev2)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
            @bot.message_handler(func=lambda message: message.text == "4 акка")
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev1 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev2 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev3 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ну, раз так хочешь... \n' +vkkiev)
                  bot.send_message(m.chat.id, vkkiev1)
                  bot.send_message(m.chat.id, vkkiev2)
                  bot.send_message(m.chat.id, vkkiev3, reply_markup=user_markup)
                  print (vkkiev+" "+vkkiev1+" "+vkkiev2+" "+vkkiev3)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
        elif vkuaresultat == '0':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Закончились, совсем. \nАкков: " + vkuaresultat, reply_markup=user_markup)
        else:
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('1 акк')
            user_markup.row('2 акка')
            user_markup.row('3 акка')
            user_markup.row('4 акка')
            user_markup.row('5 акков')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько? \nОстаток: " + vkuaresultat, reply_markup=user_markup)    
            @bot.message_handler(func=lambda message: message.text == '1 акк')
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Лови:) \n' +vkkiev)
                  bot.send_message(m.chat.id, 'Нужно будет еще что-нибудь - приходи.', reply_markup=user_markup)
                  print (vkkiev)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
            @bot.message_handler(func=lambda message: message.text == "2 акка")
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev1 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ну, два так два. Мне не жалко...\n' +vkkiev)
                  bot.send_message(m.chat.id, vkkiev1,reply_markup=user_markup)
                  print (vkkiev+' '+vkkiev1)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
            @bot.message_handler(func=lambda message: message.text == "3 акка")
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev1 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev2 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'О, мастер своего дела?;) \n' +vkkiev)
                  bot.send_message(m.chat.id, vkkiev1)
                  bot.send_message(m.chat.id, vkkiev2, reply_markup=user_markup)
                  print (vkkiev+' '+vkkiev1+' '+vkkiev2)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
            @bot.message_handler(func=lambda message: message.text == "4 акка")
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev1 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev2 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev3 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ну, раз так хочешь... \n' +vkkiev)
                  bot.send_message(m.chat.id, vkkiev1)
                  bot.send_message(m.chat.id, vkkiev2)
                  bot.send_message(m.chat.id, vkkiev3, reply_markup=user_markup)
                  print (vkkiev+" "+vkkiev1+" "+vkkiev2+" "+vkkiev3)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
            @bot.message_handler(func=lambda message: message.text == "5 акков")
            def command_text_hi(m):
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()
                  vkkiev = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev1 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev2 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev3 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  vkkiev4 = vkkiev_list.pop (0)
                  del vkkiev_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ого, а сравишься?) \n' +vkkiev)
                  bot.send_message(m.chat.id, vkkiev1)
                  bot.send_message(m.chat.id, vkkiev2)
                  bot.send_message(m.chat.id, vkkiev3)
                  bot.send_message(m.chat.id, vkkiev4, reply_markup=user_markup)
                  print (vkkiev+' '+vkkiev1+' '+vkkiev2+' '+vkkiev3+' '+vkkiev4)
                  print (vkkiev_list)
                  vkkiev = open('vkkiev.txt', 'w')
                  for index in vkkiev_list:
                        vkkiev.write(index + '\n')
                  vkkiev.close
                  vkkiev = open('vkkiev.txt', 'r+')
                  svkkiev = (vkkiev.read())
                  vkkiev_list = svkkiev.split('\n')
                  print (vkkiev_list)
                  vkkiev.close()

    @bot.message_handler(func=lambda message: message.text == "Получить мамбу МСК")
    def handle_text(message):
        #orig_mamba = open('mambaorig.txt', 'r+')
        rab_mamba = open('mamba.txt', 'r+')
        mamba_list = (rab_mamba.read())
        mambalist = mamba_list.split('\n')
        mambishche = [x for x in mambalist if x != '']
        mambaresultat = str(len(mambishche))
        print(mambaresultat)
        #omambalist = (orig_mamba.read())
        #omamba_list = omambalist.split('\n')
        #result = []
        #for index in mambishche:
        #    if index in omamba_list:
        #        result.append(index)
        #print(len(result))
        #mambaresultat = str(len(result))
#############
        if mambaresultat == '1':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Одну')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько? \nОстаток: " + mambaresultat, reply_markup=user_markup) 
            @bot.message_handler(func=lambda message: message.text == "Одну")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mamba, reply_markup=user_markup)
                    bot.send_message(m.chat.id, 'Работай хорошо, тогда у тебя всегда будут свежие и красивые аккаунты;)')
                    print (mamba)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
        elif mambaresultat == '2' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Одну')
            user_markup.row('Две')    
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько? \nОстаток: " + mambaresultat, reply_markup=user_markup) 
            @bot.message_handler(func=lambda message: message.text == "Одну")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mamba, reply_markup=user_markup)
                    bot.send_message(m.chat.id, 'Работай хорошо, тогда у тебя всегда будут свежие и красивые аккаунты;)')
                    print (mamba)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
            @bot.message_handler(func=lambda message: message.text == "Две")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]
                    mamba1 = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mamba)
                    bot.send_message(m.chat.id, mamba1, reply_markup=user_markup)
                    print (mamba)
                    print (mamba1)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
        elif mambaresultat == '3' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Одну')
            user_markup.row('Две')
            user_markup.row('Три')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько? \nОстаток: " + mambaresultat, reply_markup=user_markup)  
            @bot.message_handler(func=lambda message: message.text == "Одну")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mamba, reply_markup=user_markup)
                    bot.send_message(m.chat.id, 'Работай хорошо, тогда у тебя всегда будут свежие и красивые аккаунты;)')
                    print (mamba)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
            @bot.message_handler(func=lambda message: message.text == "Две")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]
                    mamba1 = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mamba)
                    bot.send_message(m.chat.id, mamba1, reply_markup=user_markup)
                    print (mamba)
                    print (mamba1)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
            @bot.message_handler(func=lambda message: message.text == "Три")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]
                    mamba1 = a.pop (0)
                    del a[0]
                    mamba2 = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Это уже дело)) \n '+mamba)
                    bot.send_message(m.chat.id, mamba1)
                    bot.send_message(m.chat.id, mamba2, reply_markup=user_markup)
                    print (mamba)
                    print (mamba1)
                    print (mamba2)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close() 
        elif mambaresultat == '4' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Одну')
            user_markup.row('Две')
            user_markup.row('Три')
            user_markup.row('Четыре')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько? \nОстаток: " + mambaresultat, reply_markup=user_markup)       
            @bot.message_handler(func=lambda message: message.text == "Одну")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mamba, reply_markup=user_markup)
                    bot.send_message(m.chat.id, 'Работай хорошо, тогда у тебя всегда будут свежие и красивые аккаунты;)')
                    print (mamba)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
            @bot.message_handler(func=lambda message: message.text == "Две")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]
                    mamba1 = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mamba)
                    bot.send_message(m.chat.id, mamba1, reply_markup=user_markup)
                    print (mamba)
                    print (mamba1)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
            @bot.message_handler(func=lambda message: message.text == "Три")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]
                    mamba1 = a.pop (0)
                    del a[0]
                    mamba2 = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Это уже дело)) \n '+mamba)
                    bot.send_message(m.chat.id, mamba1)
                    bot.send_message(m.chat.id, mamba2, reply_markup=user_markup)
                    print (mamba)
                    print (mamba1)
                    print (mamba2)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
            @bot.message_handler(func=lambda message: message.text == "Четыре")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]  
                    mamba1 = a.pop (0)
                    del a[0]
                    mamba2 = a.pop (0)
                    del a[0]
                    mamba3 = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Это сильно)) \n '+mamba)
                    bot.send_message(m.chat.id, mamba1)
                    bot.send_message(m.chat.id, mamba2)
                    bot.send_message(m.chat.id, mamba3, reply_markup=user_markup)
                    print (mamba)
                    print (mamba1)
                    print (mamba2)
                    print (mamba3)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    A = s.split('\n')
                    print (a)
                    f.close()
        elif mambaresultat == '0':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('На главную') 
            bot.send_message(message.chat.id, "Закончились", reply_markup=user_markup)   
        else:
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Одну')
            user_markup.row('Две')
            user_markup.row('Три')
            user_markup.row('Четыре')
            user_markup.row('Пять')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько? \nОстаток: " + mambaresultat, reply_markup=user_markup)     
            @bot.message_handler(func=lambda message: message.text == "Одну")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mamba, reply_markup=user_markup)
                    bot.send_message(m.chat.id, 'Работай хорошо, тогда у тебя всегда будут свежие и красивые аккаунты;)')
                    print (mamba)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
            @bot.message_handler(func=lambda message: message.text == "Две")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]
                    mamba1 = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Держи: \n '+mamba)
                    bot.send_message(m.chat.id, mamba1, reply_markup=user_markup)
                    print (mamba)
                    print (mamba1)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
            @bot.message_handler(func=lambda message: message.text == "Три")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]
                    mamba1 = a.pop (0)
                    del a[0]
                    mamba2 = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Это уже дело)) \n '+mamba)
                    bot.send_message(m.chat.id, mamba1)
                    bot.send_message(m.chat.id, mamba2, reply_markup=user_markup)
                    print (mamba)
                    print (mamba1)
                    print (mamba2)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
            @bot.message_handler(func=lambda message: message.text == "Четыре")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]  
                    mamba1 = a.pop (0)
                    del a[0]
                    mamba2 = a.pop (0)
                    del a[0]
                    mamba3 = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Это сильно)) \n '+mamba)
                    bot.send_message(m.chat.id, mamba1)
                    bot.send_message(m.chat.id, mamba2)
                    bot.send_message(m.chat.id, mamba3, reply_markup=user_markup)
                    print (mamba)
                    print (mamba1)
                    print (mamba2)
                    print (mamba3)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    A = s.split('\n')
                    print (a)
                    f.close()
            @bot.message_handler(func=lambda message: message.text == "Пять")
            def command_text_hi(m):
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    a = s.split('\n')
                    print (a)
                    f.close()
                    mamba = a.pop (0)
                    del a[0]  
                    mamba1 = a.pop (0)
                    del a[0]
                    mamba2 = a.pop (0)
                    del a[0]
                    mamba3 = a.pop (0)
                    del a[0]
                    mamba4 = a.pop (0)
                    del a[0]
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                    user_markup.row('На главную')
                    bot.send_message(m.chat.id, 'Ну, если ты справишься с ними... \n '+mamba)
                    bot.send_message(m.chat.id, mamba1)
                    bot.send_message(m.chat.id, mamba2)
                    bot.send_message(m.chat.id, mamba3)
                    bot.send_message(m.chat.id, mamba4, reply_markup=user_markup)
                    print (mamba)
                    print (mamba1)
                    print (mamba2)
                    print (mamba3)
                    print (mamba4)
                    print (a)
                    f = open('mamba.txt', 'w')
                    for index in a:
                          f.write(index + '\n')
                    f.close
                    f = open('mamba.txt', 'r+')
                    s = (f.read())
                    A = s.split('\n')
                    print (a)
                    f.close()


    @bot.message_handler(func=lambda message: message.text == "Получить вк МСК") 
    def handle_text(message):
        #orig_vk = open('vkorig.txt', 'r+')
        rab_vk = open('vk.txt', 'r+')
        vk_list = (rab_vk.read())
        vklist = vk_list.split('\n')
        vk_proverka = [x for x in vklist if x != '']
        vkresultat = str(len(vk_proverka))
        print(vkresultat)
        #ovk_list = (orig_vk.read())
        #ovklist = ovk_list.split('\n')
        #vkresult = []
        #for index in vk_proverka:
        #    if index in ovklist:
        #        vkresult.append(index)
        #print(vkresult)
        #print(len(vkresult))
        #vkresultat = str(len(vkresult))
        if vkresultat == '1' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('1')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Последний, заберешь? ", reply_markup=user_markup)
            @bot.message_handler(func=lambda message: message.text == "1")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Лови:) \n' +vk)
                  bot.send_message(m.chat.id, 'Нужно будет еще что-нибудь - приходи.', reply_markup=user_markup)
                  print (vk)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
        elif vkresultat == '2' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('1')
            user_markup.row('2')    
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Только две есть \nДаже докажу: " + vkresultat, reply_markup=user_markup)
            @bot.message_handler(func=lambda message: message.text == "1")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Лови:) \n' +vk)
                  bot.send_message(m.chat.id, 'Нужно будет еще что-нибудь - приходи.', reply_markup=user_markup)
                  print (vk)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
            @bot.message_handler(func=lambda message: message.text == "2")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk1 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ну, два так два. Мне не жалко...\n' +vk)
                  bot.send_message(m.chat.id, vk1,reply_markup=user_markup)
                  print (vk+' '+vk1)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
        elif vkresultat == '3' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('1')
            user_markup.row('2')
            user_markup.row('3')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько? \n Это все, что есть: " + vkresultat, reply_markup=user_markup)
            @bot.message_handler(func=lambda message: message.text == "1")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Лови:) \n' +vk)
                  bot.send_message(m.chat.id, 'Нужно будет еще что-нибудь - приходи.', reply_markup=user_markup)
                  print (vk)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
            @bot.message_handler(func=lambda message: message.text == "2")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk1 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ну, два так два. Мне не жалко...\n' +vk)
                  bot.send_message(m.chat.id, vk1,reply_markup=user_markup)
                  print (vk+' '+vk1)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
            @bot.message_handler(func=lambda message: message.text == "3")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk1 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk2 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'О, мастер своего дела?;) \n' +vk)
                  bot.send_message(m.chat.id, vk1)
                  bot.send_message(m.chat.id, vk2, reply_markup=user_markup)
                  print (vk+' '+vk1+' '+vk2)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
        elif vkresultat == '4' :
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('1')
            user_markup.row('2')
            user_markup.row('3')
            user_markup.row('4')        
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько? \nОсталось: " + vkresultat, reply_markup=user_markup)
            @bot.message_handler(func=lambda message: message.text == "1")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Лови:) \n' +vk)
                  bot.send_message(m.chat.id, 'Нужно будет еще что-нибудь - приходи.', reply_markup=user_markup)
                  print (vk)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
            @bot.message_handler(func=lambda message: message.text == "2")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk1 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ну, два так два. Мне не жалко...\n' +vk)
                  bot.send_message(m.chat.id, vk1,reply_markup=user_markup)
                  print (vk+' '+vk1)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
            @bot.message_handler(func=lambda message: message.text == "3")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk1 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk2 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'О, мастер своего дела?;) \n' +vk)
                  bot.send_message(m.chat.id, vk1)
                  bot.send_message(m.chat.id, vk2, reply_markup=user_markup)
                  print (vk+' '+vk1+' '+vk2)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
            @bot.message_handler(func=lambda message: message.text == "4")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk1 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk2 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk3 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ну, раз так хочешь... \n' +vk)
                  bot.send_message(m.chat.id, vk1)
                  bot.send_message(m.chat.id, vk2)
                  bot.send_message(m.chat.id, vk3, reply_markup=user_markup)
                  print (vk+" "+vk1+" "+vk2+" "+vk3)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
        elif vkresultat == '0' :
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Больше нет, ждите, пока зальют.", reply_markup=user_markup)   
        else :    
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('1')
            user_markup.row('2')
            user_markup.row('3')
            user_markup.row('4')
            user_markup.row('5')
            user_markup.row('На главную')
            bot.send_message(message.chat.id, "Сколько? \nВ сухом остатке у нас: " + vkresultat, reply_markup=user_markup)
            @bot.message_handler(func=lambda message: message.text == "1")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Лови:) \n' +vk)
                  bot.send_message(m.chat.id, 'Нужно будет еще что-нибудь - приходи.', reply_markup=user_markup)
                  print (vk)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
            @bot.message_handler(func=lambda message: message.text == "2")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk1 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ну, два так два. Мне не жалко...\n' +vk)
                  bot.send_message(m.chat.id, vk1,reply_markup=user_markup)
                  print (vk+' '+vk1)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
            @bot.message_handler(func=lambda message: message.text == "3")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk1 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk2 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'О, мастер своего дела?;) \n' +vk)
                  bot.send_message(m.chat.id, vk1)
                  bot.send_message(m.chat.id, vk2, reply_markup=user_markup)
                  print (vk+' '+vk1+' '+vk2)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
            @bot.message_handler(func=lambda message: message.text == "4")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk1 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk2 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk3 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ну, раз так хочешь... \n' +vk)
                  bot.send_message(m.chat.id, vk1)
                  bot.send_message(m.chat.id, vk2)
                  bot.send_message(m.chat.id, vk3, reply_markup=user_markup)
                  print (vk+" "+vk1+" "+vk2+" "+vk3)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
            @bot.message_handler(func=lambda message: message.text == "5")
            def command_text_hi(m):
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
                  vk = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk1 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk2 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk3 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  vk4 = vkmsk_list.pop (0)
                  del vkmsk_list[0]
                  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                  user_markup.row('На главную')
                  bot.send_message(m.chat.id, 'Ого, а сравишься?) \n' +vk)
                  bot.send_message(m.chat.id, vk1)
                  bot.send_message(m.chat.id, vk2)
                  bot.send_message(m.chat.id, vk3)
                  bot.send_message(m.chat.id, vk4, reply_markup=user_markup)
                  print (vk+' '+vk1+' '+vk2+' '+vk3+' '+vk4)
                  print (vkmsk_list)
                  vkmsk = open('vk.txt', 'w')
                  for index in vkmsk_list:
                        vkmsk.write(index + '\n')
                  vkmsk.close
                  vkmsk = open('vk.txt', 'r+')
                  svkmsk = (vkmsk.read())
                  vkmsk_list = svkmsk.split('\n')
                  print (vkmsk_list)
                  vkmsk.close()
			  

    if __name__=="__main__":
        bot.polling()

if __name__=="__main__":
        main()
