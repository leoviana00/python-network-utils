import json
import requests
from colorama import init, Fore, Style

def check():
    url = input("Digite a url: ")
    r = requests.get(url)
    if r.status_code == 200:
        json_object = json.loads(r.text)
        json_formatted_str = json.dumps(json_object, indent=2)
        print(Fore.GREEN + "Status da URL: " + str(r.status_code) , Style.RESET_ALL)
        print(Fore.YELLOW + "Message: " + json_formatted_str, Style.RESET_ALL)
    else:
        print(Fore.RED + "Status da URL: " + str(r.status_code) , Style.RESET_ALL)   
        print(Fore.YELLOW + "Message: " + r.text, Style.RESET_ALL) 