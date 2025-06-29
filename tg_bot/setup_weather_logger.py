import logging
import os 

def setup_logger():
    os.makedirs(f"{os.getcwd()}/tg_bot/logs", exist_ok= True)
    logger = logging.getLogger("weather_app")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        file_handler = logging.FileHandler(f"{os.getcwd()}/tg_bot/logs/info.log", encoding="utf-8")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


