# Módulos externos
import logging
from colorama import init, Fore, Style
init()
from src.date import dateFormatted
from datetime import datetime

# Módulos internos
from src.scanport import scan
from src.ping import ping
from src.healthcheck import check
from src.logger import finish, start 

# Creando logger
logging.basicConfig(filename='logs/scanner.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#Criando console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Criando formato
formatter = logging.Formatter( dateFormatted() + ' %(name)s - %(levelname)s - %(message)s')

# add formato ao ch
ch.setFormatter(formatter)

# add ch ao logger
logger.addHandler(ch)

# Menu
while True:

    h1 = datetime.now()
    print(Fore.GREEN +'# ========================================================', Style.RESET_ALL)
    print(Fore.GREEN +'#  🚀 Menu:       NETWORK MANAGEMENT', Style.RESET_ALL)
    print(Fore.GREEN +'#  😎 Author:   Leonardo Viana Pereira', Style.RESET_ALL)
    print(Fore.GREEN +f'#  ⏲️  Time:   {h1}', Style.RESET_ALL)
    print(Fore.GREEN +'# ========================================================', Style.RESET_ALL)
    print(Fore.YELLOW +'➊ - Port Scan ', Style.RESET_ALL)
    print(Fore.YELLOW +'➋ - Ping Test ', Style.RESET_ALL)
    print(Fore.YELLOW +'➌ - Health Check ', Style.RESET_ALL)
    print(Fore.YELLOW +'➒ - Sair ', Style.RESET_ALL)
    start()
    try:    
        option_choice = input('Escolha uma das opções acima: ')
        logger.info(f'👆 Opção {option_choice} ecolhida')
        option_choice = int(option_choice)
        
    except ValueError:
        print("Nenhum número inteiro válido! Por favor, tente novamente ... ")
        logger.error(f'O {option_choice} não é um número inteiro válido! Por favor, tente novamente ... ')
    if option_choice == 1:
        print(Fore.GREEN +'# ========================================================', Style.RESET_ALL)
        print(Fore.GREEN +'❇️ 🔍 Scanner de porta usando soquete', Style.RESET_ALL)
        print(Fore.GREEN +'# ========================================================', Style.RESET_ALL)
        scan()
    elif option_choice == 2:
        print(Fore.GREEN +'# ========================================================', Style.RESET_ALL)
        print(Fore.GREEN +'❇️ 🤖 Scanner de porta usando varredura TCP', Style.RESET_ALL)
        print(Fore.GREEN +'# ========================================================', Style.RESET_ALL)
        ping()
    elif option_choice == 3:
        print(Fore.GREEN +'# ========================================================', Style.RESET_ALL)
        print(Fore.GREEN +f'❇️ 🌐 Testar uma rota tipo GET', Style.RESET_ALL)
        print(Fore.GREEN +'# ========================================================', Style.RESET_ALL)
        check()
    elif option_choice == 9:
        print('Operação finalizada com sucesso!')
        logger.info('Finished')
        finish()
        break
    else:
        print('Você não digitou uma opção válida! Por favor, tente novamente ... ')
        logger.error(f'O {option_choice} não é uma opção válida! Por favor, tente novamente ... ')

def main():
    # 'application' code
    logger.info('Started')
    # logger.info('Finished')
    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warning('warn message')
    # logger.error('error message')
    # logger.critical('critical message')


if __name__ == '__main__':
    main()