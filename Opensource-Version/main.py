import os
import json
import requests
import sys
from colorama import init
init()
from colorama import Fore
import time
from time import sleep
from datetime import datetime
os.system('title Luya-Tokeninfo - https://t.me/bladetools')
mtxt = Fore.YELLOW + """                                  ▄█       ███    █▄  ▄██   ▄      ▄████████                             
                                 ███       ███    ███ ███   ██▄   ███    ███                             
                                 ███       ███    ███ ███▄▄▄███   ███    ███                             
                                 ███       ███    ███ ▀▀▀▀▀▀███   ███    ███                             
                                 ███       ███    ███ ▄██   ███ ▀███████████                             
                                 ███       ███    ███ ███   ███   ███    ███                             
                                 ███▌    ▄ ███    ███ ███   ███   ███    ███                             
                                 █████▄▄██ ████████▀   ▀█████▀    ███    █▀                              
                                ▀                                                                       
            ███      ▄██████▄     ▄█   ▄█▄    ▄████████ ███▄▄▄▄    ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
        ▀█████████▄ ███    ███   ███ ▄███▀   ███    ███ ███▀▀▀██▄ ███  ███▀▀▀██▄   ███    ███ ███    ███ 
           ▀███▀▀██ ███    ███   ███▐██▀     ███    █▀  ███   ███ ███▌ ███   ███   ███    █▀  ███    ███ 
            ███   ▀ ███    ███  ▄█████▀     ▄███▄▄▄     ███   ███ ███▌ ███   ███  ▄███▄▄▄     ███    ███ 
            ███     ███    ███ ▀▀█████▄    ▀▀███▀▀▀     ███   ███ ███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
            ███     ███    ███   ███▐██▄     ███    █▄  ███   ███ ███  ███   ███   ███        ███    ███ 
            ███     ███    ███   ███ ▀███▄   ███    ███ ███   ███ ███  ███   ███   ███        ███    ███ 
           ▄████▀    ▀██████▀    ███   ▀█▀   ██████████  ▀█   █▀  █▀    ▀█   █▀    ███         ▀██████▀  
                                 ▀                                                                       """
os.system('cls')
print(mtxt)
print(Fore.WHITE + "  [", end="")
print(Fore.YELLOW + ">", end="")
print(Fore.WHITE + "] Target-Discord-Token: ", end="")
tokn = input("")
time.sleep(2)

headr1 = {
    'Authorization': f'{tokn}',
    'Content-Type': 'application/json'
}
res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headr1)
if res.status_code == 200:
    print(Fore.GREEN + "  [+] Token valid! Collecting data!")
    pass
else:
    print(Fore.RED + "  [!] Error: Invalid Token")
    time.sleep(2)
    sys.exit()

res_json = res.json()
user = f'{res_json["username"]}#{res_json["discriminator"]}'
uid = res_json['id']
user_id = uid
avatar_id = res_json['avatar']
avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
pnum = res_json['phone']
email = res_json['email']
mfa_enabled = res_json['mfa_enabled']
flags = res_json['flags']
lang = res_json['locale']
verified = res_json['verified']
creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
has_nitro = False
res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headr1)
nitro_data = res.json()
has_nitro = bool(len(nitro_data) > 0)
os.system('cls')
print(Fore.WHITE + f"""\n
Token: {tokn}
Username: {user}
User-ID: {uid}
Avatar-ID: {avatar_id}
Avatar-URL: {avatar_url}
Phone-Number: {pnum}
Email: {email}
2FA: {mfa_enabled}
Flags: {flags}
Language: {lang}
Verified: {verified}
Creation Date: {creation_date}
Nitro: {has_nitro}
""")

exiiit = input("")