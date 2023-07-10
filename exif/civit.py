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
import pyautogui
import pymysql
import datetime

#sql save
def picture_inser(conn,cursor, dict, name):
    ts=time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    try:
        sql = f'''INSERT INTO civit_data (user_id, name, file_link, prompt, negative_prompt,timestamp,steps,sampler,cfg_scale,seed,model_hash,clip_skip,denoising_strength) 
        VALUES ("admin","{name}","{name}","{dict['prompt']}","{dict['negative'] if 'negative' in dict else "NULL"}",
        "{timestamp}",{dict['Steps'] if 'Steps' in dict else "NULL"} ,"{dict['Sampler'] if 'Sampler' in dict else "NULL"}",
        {dict['CFGscale'] if 'CFGscale' in dict else "NULL"},"{dict['Seed'] if 'Seed' in dict else "NULL"}",
        "{dict['Modelhash'] if 'Modelhash' in dict else "NULL"}",{dict['Clipskip'] if 'Clipskip' in dict else "NULL"},
        "{dict['Denoisingstrength'] if 'Denoisingstrength' in dict else "NULL"}");'''
        print("sql : ",sql)
        cursor.execute(sql)
        conn.commit()
    except:
        print("error")

conn = pymysql.connect(host='15.164.231.65', port=51143, user='grim', password='1111', db='grim', charset='utf8')
cursor = conn.cursor()

#civit ai 크롤링 위치 설정
tagnum=4
home="https://civitai.com/images"
tagurl="https://civitai.com/images?tags="+str(tagnum)+"&view=feed"

#safari 창 크기 설정 및 시작
driver=webdriver.Safari()
driver.maximize_window()
driver.get(tagurl)

#week를 all time으로 수동 변경
time.sleep(5)
print(pyautogui.position())
pyautogui.moveTo(2365,175)
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(2365,400)
pyautogui.click()
time.sleep(3)

diction=[]
name_set=set()
head=["id","name","file_link","prompt","negative_prompt","size","steps","sampler","cfg_scale","seed","model_hash","clip_skip","denoising_strentgh"]

#page_down을 40회 반복
count=1
body=driver.find_element(By.CSS_SELECTOR,'body')
while count<40:
    count+=1
    #page_down 후 이미지 로딩 대기
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(5)

    #페이지 확인
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    main=soup.find('main')
    
    #페이지 속 img tag 찾기
    imgs=main.find_all("img")
    for img in imgs:
        if "src" in str(img):
            #img가 src가 있으면 src에서 원본 주소 구하기
            url=img.get("src")
            print(url)
            response=requests.get(url,stream=True)

            #이미지 이름을 통해 중복 여부 검사
            name_id=url.split('/')
            name_=name_id[len(name_id)-1]
            if name_ in name_set:
                continue
            name_set.add(name_)
            if "gif" in name_:
                continue

            #get exif
            if response.status_code == 200:
                image=Image.open(response.raw)
                if 'Gif' in str(type(image)) :
                    continue
                exif_data = image._getexif()
                taglabel={}
                dict={}
                if exif_data:
                    for tag, value in exif_data.items():
                        decoded = TAGS.get(tag,tag)
                        taglabel[decoded]=value
                    if 'UserComment' not in taglabel:
                        continue
                    
                    #UserComment 분석
                    data=str(taglabel['UserComment'])
                    data=data.replace("b'UNICODE",'')
                    data=data.replace("b\"UNICODE",'')
                    data=data.replace("\\x00",'')
                    data=data.replace("\"","")
                    take=data.split('\\n')

                    #get prompt
                    dict["prompt"]=take[0]
                    #get negative
                    if len(take)<2:
                        continue
                    negative=take[1].split(':')
                    try:
                        ne_prom=negative[1]
                        if negative[0] == "Negative prompt":
                            for neg in negative[2:]:
                                ne_prom=ne_prom+':'+neg
                            dict["negative"]=ne_prom
                        else:
                            else_data=take[1].replace('\'','')
                            else_data=else_data.replace('\"','')
                            else_data=else_data.replace(' ','')
                            else_data=else_data.split(',')
                            for eld in else_data:
                                if ':' in eld and len(eld.split(':'))==2:
                                    datakey,datavalue = eld.split(':')
                                    dict[datakey]=datavalue
                    except:
                        dict["negative"]=negative
                    # else data
                    try:
                        else_data=take[2].replace('\'','')
                        else_data=else_data.replace(' ','')
                        else_data=else_data.split(',')
                        for eld in else_data:
                            if ':' in eld and len(eld.split(':'))==2:
                                datakey,datavalue = eld.split(':')
                                dict[datakey]=datavalue
                    except:
                        dict["Sample"]="NULL"
                    print(dict)
                    temp_dic=["admin",name_,url,dict['prompt'],dict['negative']if "negative" in dict else "NULL",dict['Size'] if "Size" in dict else "NULL",
                                dict['Steps'] if "Steps" in dict else "NULL",dict['Sampler'] if "Sampler" in dict else "NULL",dict['CFGscale'] if "CFGscale" in dict else "NULL",
                                dict['Seed'] if "Seed" in dict else "NULL",dict['Modelhash'] if "Modelhash" in dict else "NULL",
                                dict['Clipskip'] if "Clipskip" in dict else 2,dict['Denoisingstrength'] if "Denoisingstrength" in dict else "NULL"]
                    if temp_dic[5] == "NULL" or 'nsfw' in str(temp_dic[3]) or 'Negative' in str(temp_dic[3]) or 'NSFW' in str(temp_dic[3]):
                        continue
                    #sql save
                    picture_inser(conn,cursor,dict,url)