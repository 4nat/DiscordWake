#THIS PROJECT MADE BY 4NAT
#Discord : sehza#0001
#ANY QUESTION > instagram/@ichbinharun  
import requests
import os 
import time
count=0
countt=0
URL= input('Enter Your Glitch URL > ')
sleep=int(input('Enter Time (Seconds) Default 180=3min > '))
try:
  while True:
    os.system('clear')
    count += 1
    r=requests.get(URL)
    if r.status_code == 200:
        print(URL,'Request Success. = ',count,'Times')
    else:countt += 1;print(URL,'Request Fail! = ',countt,'Times')
    print('\nMADE BY 4NaT\n')
    print('TOTAL SUCCESS = ',count)
    print('TOTAL FAIL    = ',countt ) 
    time.sleep(sleep)
except:
  print('Error :/')
#</>#</>#</>#</>#</>#</>#</>#</>#</>#</>
