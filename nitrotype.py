'''
nitrotype account creator made by faint

note: if theres no comment dont change it
'''

import requests
import json
import random
import thread6
import colorama

colorama.init()

amount = input('How many accounts do you want to create? ')

def main():
    for i in range(int(amount)):
        url = "https://www.nitrotype.com/api/v2/auth/register/username"
        
        username = f"FaintRunsYou{random.randint(1,99999)}" # change if you want

        payload = json.dumps({
        "username": username,
        "password": "Dorsey83!", # change if you want
        "acceptPolicy": "on",
        "receiveContact": "",
        "tz": "America/Chicago",
        "qualifying": 1,
        "avgSpeed": 260, # change if you want
        "avgAcc": 100, # change if you want
        "raceSounds": "only_fx",
        })
        headers = {
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Cookie': '__cf_bm=fZKUyeRnSSJd_.hInxcFMrR2E2RynWKWIue2Rca10G8-1693629957-0-AeNEXiGUEVW4GAhu8iK2vrbVF7GtE0x9fyJ0cBhTbNHhU4BPeHulp+9zk29Hcoqo+th2q0ac0CcG7byjx6DwP1k=; _cfuvid=yTvFeL5CIMYBfewNyFnK.0gb9PZ3egazK32zYe0grz4-1693629957628-0-604800000; nitrodev=36ac2187-34bd-4cdb-8837-fd3ea411c3ea; ntdev=208053530'
        }
        response = requests.request("POST", url,headers=headers, data=payload)
        
        with open('accounts.txt','+a') as f:
            f.write(f'{{}}:Dorsey83!\n'.format(username))

        print(f'{{}}{{}} created!'.format(colorama.Fore.LIGHTGREEN_EX, username))

if __name__ == '__main__':
    thread6.run_threaded(main)
