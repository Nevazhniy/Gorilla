import requests
import time
import webbrowser
from random import randint
input('Сейчас вы перейдёте по ссылке и нажмёте "Разрешить" \n чтобы получить access_token, скопируйте его из ссылки')
webbrowser.open('https://oauth.vk.com/authorize?client_id=6121396&scope=69634&redirect_uri=https://api.vk.com/blank.html&display=page&response_type=token&revoke=1')
access_token = input('access_token: ')
bet = input('Ставка: ')
firstDelay = int(input('Рандомная задержка в регионе от: '))
secondDelay = int(input('до: '))
url = f'https://api.vk.com/method/messages.send?user_id=-171493284&message=азино {bet}&v=5.9&access_token={access_token}'
while True:
    request = requests.get(url=url)
    if 'response' in request.text:
        count = count + 1
        print(f'Bet №{count}')
    elif 'captcha needed' in request.text:
        print('captcha')
        time.sleep(10)
    time.sleep(randint(firstDelay, secondDelay))
