import os
import asyncio
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters,
    ConversationHandler, ContextTypes
)
from dotenv import load_dotenv

# Загрузка токена из .env, если есть
load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN') or '7886967900:AAHpgOBklkqQwVaO5aCJTdMi11ELjyHzoj8'

# Состояния FSM
(ASK_NAME, ASK_PHONE, ASK_YOGA, ASK_INTENSITY, ASK_TIME, CHOOSE_CLASS, FINAL_INFO) = range(7)

# Варианты для кнопок
YOGA_EXPERIENCE = ["Да", "Нет"]
INTENSITY = ["Поинтенсивней", "Поспокойней"]
TIME_OPTIONS = ["Будни утро", "Будни вечер", "Выходные", "Индивидуально"]
# Примерные занятия (можно заменить на реальные)
CLASSES = ["Пн 19:00 — Хатха-йога", "Сб 12:00 — Виньяса", "Вс 10:00 — Йога-нидра"]

ADMIN_LINK = "https://t.me/your_admin_username"  # Заменить на реальный username администратора
CHANNEL_LINK = "https://t.me/sokolnikiyoga"
SITE_LINK = "https://prakritiyoga.ru/"
PAY_LINK = "https://www.sberbank.com/sms/pbpn?requisiteNumber=79162565675"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Приветствую в чатботе Prakriti! Перед тем как записаться на занятие, необходимо пройти небольшой опрос — чтобы определить подходящее для вас занятие, ответьте, пожалуйста, на вопросы ниже"
    )
    await asyncio.sleep(0.03)
    await update.message.reply_text("Как вас зовут?")
    return ASK_NAME

async def ask_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['name'] = update.message.text.strip()
    await update.message.reply_text("Пожалуйста, укажите ваш номер телефона для связи.")
    return ASK_PHONE

async def ask_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['phone'] = update.message.text.strip()
    keyboard = [[KeyboardButton(text=opt)] for opt in YOGA_EXPERIENCE]
    await update.message.reply_text(
        "Занимались раньше йогой?",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    return ASK_YOGA

async def ask_yoga(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['yoga_experience'] = update.message.text.strip()
    keyboard = [[KeyboardButton(text=opt)] for opt in INTENSITY]
    await update.message.reply_text(
        "Хотите поинтенсивней или поспокойней?",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    return ASK_INTENSITY

async def ask_intensity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['intensity'] = update.message.text.strip()
    keyboard = [[KeyboardButton(text=opt)] for opt in TIME_OPTIONS]
    await update.message.reply_text(
        "Когда рассматриваете занятия?",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    return ASK_TIME

async def ask_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['time'] = update.message.text.strip()
    await update.message.reply_text(
        "По итогу опроса мы подготовили для вас наиболее подходящие занятия!\n\nЗДЕСЬ ПОКА ЗАГЛУШКА, В БУДУЩЕМ ТУТ БУДЕТ ПОДРОБНОСТИ О ЗАНЯТИИ, ВРЕМЯ, ИНТЕНСИВНОСТЬ И ПРОЧЕЕ\n\nДля того, чтобы записаться на занятие, нажми на одну из кнопок внизу",
        reply_markup=ReplyKeyboardMarkup([[c] for c in CLASSES], one_time_keyboard=True, resize_keyboard=True)
    )
    return CHOOSE_CLASS

async def choose_class(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['chosen_class'] = update.message.text.strip()
    info = (
        "Записал тебя! Держи подробную информацию которая может тебе пригодиться :)\n"
        "\nАдрес:\nСокольнический вал 1Б\nЛедовый дворец, сектор Б\nОгибаете здание слева, вход с торца, лифт справа, как вошли\n5 этаж, из лифта направо, дверь с надписью «Облачные врата»"
        "\n\nЧто взять с собой:\n- Удобная форма одежды (легинсы, футболка/майка)\n- Занимаемся босиком\n- Все оборудование есть в зале"
        "\n\nОплата:\n- После урока наличными или переводом\n- Ссылка для оплаты: " + PAY_LINK + "\n- Для других банков: перевод по номеру телефона"
        "\n\nДополнительно:\n- Ссылка на Telegram-канал: " + CHANNEL_LINK + "\n- Ссылка на сайт: " + SITE_LINK
    )
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Связаться с администратором", url=ADMIN_LINK)]
    ])
    await update.message.reply_text(info, reply_markup=keyboard)
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Диалог завершён. Если захотите записаться — напишите /start.")
    return ConversationHandler.END

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_name)],
            ASK_PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_phone)],
            ASK_YOGA: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_yoga)],
            ASK_INTENSITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_intensity)],
            ASK_TIME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_time)],
            CHOOSE_CLASS: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_class)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    app.add_handler(conv_handler)
    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    app.run_polling()

if __name__ == '__main__':
    main() 