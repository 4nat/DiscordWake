import requests
import os 
import time

a=requests.get('https://peakhackersnet.glitch.me/')
b=requests.get('https://peakhackersspot.glitch.me/')
os.system('clear')
if a.status_code == 200:
    print('Netflix Request Success.')
else:print('Spotify Request Fail!')
if b.status_code == 200:
    print('Spotify Request Success.')
else:print('Spotify Request Fail!')

time.sleep(180)
