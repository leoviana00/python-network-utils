from logging import Logger
from src.date import dateFormatted


def start():
    Logger('Start!')
    logger_file = open("./logs/app.log", "a", encoding='utf-8')
    logger_file.write(dateFormatted() + ' - Programa inicializado ...\n')
    logger_file.close()

def finish():
    Logger('Finish!')
    logger_file = open("./logs/app.log", "a", encoding='utf-8')
    logger_file.write(dateFormatted() + ' - Programa finalizado ...\n')
    logger_file.close()

    