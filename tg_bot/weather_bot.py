import os
from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
from current_weather import get_current_weather
from setup_weather_logger import setup_logger
from load_dotenv import load_dotenv

load_dotenv()


class WeatherBot:
    def __init__(self):
        self.weather_logger = setup_logger()
        self.weather_logger.info("The bot has been launched")

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """вывод команды /start в боте"""
        await update.message.reply_text("Hi, I'm the weather bot. Use /weather")
        self.weather_logger.info("The 'start' function has been called")

    async def weather_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Ручная проверка погоды"""
        weather_text = get_current_weather(os.getenv("CITY"), os.getenv("API_KEY"))
        await update.message.reply_text(weather_text)
        self.weather_logger.info("The 'weather' function has been called")

    async def send_daily_weather(self, context: CallbackContext):
        """Автоматическая отправка погоды в группу"""
        weather_text = get_current_weather(os.getenv("CITY"), os.getenv("API_KEY"))
        await context.bot.send_message(
            chat_id=os.getenv("GROUP_CHAT_ID"), text=weather_text
        )
