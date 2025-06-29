from telegram.ext import Application, CommandHandler
from setup_weather_logger import setup_logger
import datetime
from weather_bot import WeatherBot

weather_logger = setup_logger()
weather_logger.info("The bot has been launched")


if __name__ == "__main__":
    weather_bot = WeatherBot()
    application = (
        Application.builder()
        .token("7784794264:AAEeqTPg1c07KFw3neyeykVlISGUqOEaFSE")
        .build()
    )

    application.add_handler(CommandHandler("start", weather_bot.start))
    application.add_handler(CommandHandler("weather", weather_bot.weather_command))

    job_queue = application.job_queue
    job_queue.run_daily(
        weather_bot.send_daily_weather,
        time=datetime.time(hour=0, minute=0, tzinfo=datetime.timezone.utc),
        days=(0, 1, 2, 3, 4, 5, 6),
    )
    application.run_polling()
