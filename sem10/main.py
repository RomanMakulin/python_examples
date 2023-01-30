import time
import logging
from aiogram import Bot, Dispatcher, executor, types
from random import randint


# 'UTF-8-sig'
logging.basicConfig(level=logging.INFO, filename="bot_log.csv", filemode="w",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")

MSG = "{}, выбери категорию: "

bot = Bot("5776394325:AAG0QECIgfzKHPH-Owc_-I9PR5AIa9W3SPo")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    user_bot = message.from_user.is_bot
    user_message = message.text
    logging.info(f'{user_id=} {user_bot=} {user_message=}')
    await message.reply(f"Привет, {user_name}, я бот, помогающий с выбором фильма!")
    time.sleep(1)
    btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/Фильмы')
    btn2 = types.KeyboardButton('/Мультики')
    btns.add(btn1, btn2)
    await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)

@dp.message_handler(commands=['Фильмы'])
async def func(message: types.Message):
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_fantasy = types.KeyboardButton('/Фантастика')
        btn_horror = types.KeyboardButton('/Ужасы')
        btn_camedy = types.KeyboardButton('/Комедия')
        btn_roman = types.KeyboardButton('/Романтика')
        btn_historic = types.KeyboardButton('/Военные')
        btn_dogs = types.KeyboardButton('/Про_собак')
        back = types.KeyboardButton("/Меню")
        btns.add(btn_fantasy, btn_horror, btn_camedy, btn_roman, btn_historic, btn_dogs, back)
        await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)

@dp.message_handler(commands=['Мультики'])
async def func(message: types.Message):
        await bot.send_message(message.from_user.id, f'Подобрал на свой вкус: {mults[randint(0, len(mults))]}')

@dp.message_handler(commands=['Меню'])
async def menu_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'Возвращаемся в меню искать что-то новенькое!')
    user_id = message.from_user.id
    user_name = message.from_user.first_name 
    btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/Фильмы')
    btn2 = types.KeyboardButton('/Мультики')
    btns.add(btn1, btn2)
    await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)

fantasy = ['Гарри Поттер', 'Аватар', 'Властелин кольца', 'Звездные войны', 'Люди Икс', 'Человек Паук', 'Мстители']
horror = ['Дом 2', 'Пиковая дама', 'Астрал']
camedy = ['Американский пирог', 'Дружить по-русски', 'Очень страшное кино']
roman = ['Титаник', 'Елки', 'После']
historic = ['9 рота', 'Брестская крепость']
mults = ['Ледниковый период', 'Душа', 'Головоломка']
dogs = ['Собака 1', 'Собака 2', 'Собака 3']

@dp.message_handler(commands=['Фантастика'])
async def fantasy_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Подобрал на свой вкус: {fantasy[randint(0, len(fantasy))]}')

@dp.message_handler(commands=['Ужасы'])
async def horror_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Подобрал на свой вкус: {horror[randint(0, len(horror))]}')

@dp.message_handler(commands=['Комедия'])
async def comedy_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Подобрал на свой вкус: {camedy[randint(0, len(camedy))]}')

@dp.message_handler(commands=['Романтика'])
async def roman_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Подобрал на свой вкус: {roman[randint(0, len(roman))]}')
    
@dp.message_handler(commands=['Военные'])
async def historic_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Подобрал на свой вкус: {historic[randint(0, len(historic))]}')

@dp.message_handler(commands=['Про_собак'])
async def dogs_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Подобрал на свой вкус: {dogs[randint(0, len(dogs))]}')

if __name__ == '__main__':
    executor.start_polling(dp)