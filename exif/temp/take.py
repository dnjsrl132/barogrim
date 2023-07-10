from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from PIL.ExifTags import TAGS
import requests
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time
#from selenium.webdriver.support.wait import WebdriverWait
#from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import datetime

ts = time.time()        
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(len(timestamp))









'''
#url="https://www.ptsearch.info/articles/list_best/?page=1&week=37"
home="https://civitai.com/images"
tagurl="https://civitai.com/images?tags=5193&view=feed"
#url="https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/a78a4bd3-b662-4587-893b-207a3abf9ec9/width=450/01576-132340236-8k%20portrait%20of%20beautiful%20cyborg%20with%20brown%20hair,%20intricate,%20elegant,%20highly%20detailed,%20majestic,%20digital%20photography,%20art%20by%20artg.jpeg"
driver=webdriver.Safari()
driver.maximize_window()
driver.get(tagurl)

#driver.get(home)
#driver.implicitly_wait(500)
#time.sleep(5)

url="https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f22fa6fe-6c6f-44e0-632b-339e83675600/width=450/168139.jpeg"
response=requests.get(url,stream=True)

if response.status_code == 200:
    image=Image.open(response.raw)
    exif_data = image._getexif()
    taglabel={}
    dict={}
    if exif_data:
        for tag, value in exif_data.items():
            decoded = TAGS.get(tag,tag)
            taglabel[decoded]=value
    print(taglabel)



print(pyautogui.position())
pyautogui.moveTo(2365,175)
pyautogui.click()
time.sleep(5)
pyautogui.moveTo(2365,400)
pyautogui.click()

week=driver.find_element(By.LINK_TEXT,"WEEK")
week.click()
'''




#week=WebdriverWait(driver,10).until(
#week=EC.presence_of_element_located((By.LINK_TEXT, "WEEK"))
#week.click()
#alltime=WebdriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "ALL TIME")))
#alltime.click()

'''
diction=[]
head=["id","name","file_link","prompt","negative_prompt","size","steps","sampler","cfg_scale","seed","model_hash","clip_skip","denoising_strentgh"]
body=driver.find_element(By.CSS_SELECTOR,'body')
play=1
while play<5:
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    #temp=driver.find_element(By.CSS_SELECTOR,f'body > main > div.container > div:nth-child(2) > a > img')
    main=soup.find('main')
    #print(main)
    #imgs=driver.find_elements(By.TAG_NAME,"img")
    imgs=main.find_all("img")
    print(len(imgs))
    if len(imgs)>100:
        break
print(len(imgs))
txt='body > main > div.container > div:nth-child(2) > a'
temp=driver.find_element(By.CSS_SELECTOR,f'{txt}').get_attribute("href")
print(temp)

n=1
while driver.find_element(By.CLASS_NAME,"manine-c9tsgh") and n<10:
    temp = driver.find_element(By.CLASS_NAME,"manine-c9tsgh").get_attribute("href")
    print(temp)
    n=n+1
'''
