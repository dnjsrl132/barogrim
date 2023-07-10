from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from PIL import Image
from PIL.ExifTags import TAGS
import requests
import pandas as pd
import pymysql
import time
import datetime

#img tag 확인
def drivercheck(driver,num):
    try:
        driver.find_element(By.CSS_SELECTOR,f'body > main > div.container > div:nth-child({cursor_num}) > a > img')
        return True
    except:
        return False
#img가 있는지 확인
def imgcheck(driver):
    try:
        turl=driver.find_element(By.CSS_SELECTOR,'body > main > div.container > div:nth-child(7) > img').get_attribute("src")
    except:
        turl="NULL"
    return turl

#sql save
def picture_inser(conn,cursor, dict, name):
    ts=time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    sql = f'''INSERT INTO picture_data (user_id, name, file_link, prompt, negative_prompt,timestamp,steps,sampler,cfg_scale,seed,model_hash,clip_skip,denoising_strength) 
    VALUES ("admin","{name}","{name}","{dict['prompt']}","{dict['negative'] if 'negative' in dict else "NULL"}",
    "{timestamp}",{dict['Steps'] if 'Steps' in dict else "NULL"} ,"{dict['Sampler'] if 'Sampler' in dict else "NULL"}",
    {dict['CFGscale'] if 'CFGscale' in dict else "NULL"},{dict['Seed'] if 'Seed' in dict else "NULL"},
    "{dict['Modelhash'] if 'Modelhash' in dict else "NULL"}",{dict['Clipskip'] if 'Clipskip' in dict else "NULL"},
    {dict['Denoisingstrength'] if 'Denoisingstrength' in dict else "NULL"});'''
    print("sql : ",sql)
    cursor.execute(sql)
    conn.commit()

conn = pymysql.connect(host='15.164.231.65', port=51143, user='grim', password='1111', db='grim', charset='utf8')
cursor = conn.cursor()

#start
week_start=37 #start week set
home = "http://www.ptserach.info"
driver=webdriver.Safari()
file_name="data.xlsx"

#week 별 page 확인
for week in range(week_start):
    diction=[]
    for page in range(12):
        url="https://www.ptsearch.info/articles/list_best/?page="+str(page+1)+"&week="+str(week_start-week)
        print(url)
        driver.get(url)
        if driver.title=="Not Found":
            break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')

        cursor_num=2   #week_best의 이미지 넘버
        head=["id","name","file_link","prompt","negative_prompt","size","steps","sampler","cfg_scale","seed","model_hash","clip_skip","denoising_strentgh"]

        #find pic
        while drivercheck(driver,cursor_num) and cursor_num < 20:
            print(url)
            #img의 원본 주소 가져오기
            temp = driver.find_element(By.CSS_SELECTOR,f'body > main > div.container > div:nth-child({cursor_num}) > a').get_attribute("href")
            print(temp)
            cursor_num+=1
            driver.get(temp)
            
            turl=imgcheck(driver)
            if "NULL" in turl:
                continue
            print(turl)
            time.sleep(1)

            #다시 원본으로 돌아가기
            driver.get(url)
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')

            #jpg 파일 찾기
            if 'jpg' not in turl:
                continue
            response=requests.get(turl,stream=True)
            #get name
            name_id=turl.split('/')
            name_=name_id[len(name_id)-1]
            #get exif
            if response.status_code == 200:
                image=Image.open(response.raw)
                exif_data = image._getexif()
                taglabel={}
                dict={}
                if exif_data:
                    for tag, value in exif_data.items():
                        decoded = TAGS.get(tag,tag)
                        taglabel[decoded]=value
                    if 'UserComment' not in taglabel:
                        continue
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
                    #else data
                    try:
                        else_data=take[2].replace('\'','')
                        else_data=else_data.replace(' ','')
                        else_data=else_data.replace('\"','')
                        else_data=else_data.split(',')
                        for eld in else_data:
                            if ':' in eld and len(eld.split(':'))==2:
                                datakey,datavalue = eld.split(':')
                                dict[datakey]=datavalue
                    except:
                        dict["Sample"]="NULL"
                    print(dict)
                    temp_dic=["admin",name_,turl,dict['prompt'],dict['negative']if "negative" in dict else "NULL",dict['Size'] if "Size" in dict else "NULL",
                              dict['Steps'] if "Steps" in dict else "NULL",dict['Sampler'] if "Sampler" in dict else "NULL",dict['CFGscale'] if "CFGscale" in dict else "NULL",
                              dict['Seed'] if "Seed" in dict else "NULL",dict['Modelhash'] if "Modelhash" in dict else "NULL",
                              dict['Clipskip'] if "Clipskip" in dict else "NULL",dict['Denoisingstrength'] if "Denoisingstrength" in dict else "NULL"]
                    if temp_dic[5] == "NULL" or 'nsfw' in str(temp_dic[3]) or 'Negative' in str(temp_dic[3]):
                        continue
                    #sql save
                    picture_inser(conn,cursor,dict,turl)
            else:
                print("non")
