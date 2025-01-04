import os
import json
from dotenv import load_dotenv
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Загружаем переменные окружения
load_dotenv()

# Получаем токен бота и URL веб-приложения из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBAPP_URL = os.getenv('WEBAPP_URL')

if not BOT_TOKEN:
    raise ValueError("Необходимо указать BOT_TOKEN в файле .env")
if not WEBAPP_URL:
    raise ValueError("Необходимо указать WEBAPP_URL в файле .env")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    # Создаем кнопку для открытия веб-приложения
    keyboard = [[InlineKeyboardButton(
        text="Открыть приложение",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправляем приветственное сообщение с кнопкой
    await update.message.reply_text(
        "Привет! Нажмите на кнопку ниже, чтобы открыть приложение:",
        reply_markup=reply_markup
    )

async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик данных от веб-приложения"""
    try:
        # Получаем данные из веб-приложения
        data = json.loads(update.effective_message.web_app_data.data)
        
        # Отправляем сообщение обратно пользователю
        if 'message' in data:
            await update.message.reply_text(f"Вы отправили: {data['message']}")
    except Exception as e:
        print(f"Ошибка при обработке данных: {e}")
        await update.message.reply_text("Произошла ошибка при обработке данных")

def main():
    """Основная функция запуска бота"""
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))

    # Запускаем бота
    print("Бот запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
