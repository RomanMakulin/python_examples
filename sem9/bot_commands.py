from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi - приветствие\n/help - помощь по командам\n/sum - сумма чисел (вводить сколько угодно через пробел)\n/sorting - сортировка элементов (вводить сколько угодно через пробел)')


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Yo, dear {update.effective_user.first_name}!')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    items = update.message.text.split()
    result = 0
    for i in items:
        if i.isdigit():
            result += int(i)
    await update.message.reply_text(f'Сумма чисел = {result}')

async def sorting_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    items = update.message.text.split()
    a = map(int, filter(str.isdigit, items))
    await update.message.reply_text(f'{", ".join(map(str,sorted(a)))}')