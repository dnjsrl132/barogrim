from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from PIL import Image
from PIL.ExifTags import TAGS
import requests
import pandas as pd

#start
home = "https://civitai.com"
diction=[]

page=0
url=home
print(url)

driver=webdriver.Safari()
driver.get(url)
driver.implicitly_wait(3)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')

cursor_num=2   #cursor_num = 1

head=["id","name","file_link","prompt","negative_prompt","timestamp","steps","sampler","cfg_scale","seed","model_hash","clip_skip","denoising_strentgh"]

#find pic
while driver.find_element(By.CSS_SELECTOR,f'body > main > div.container > div:nth-child({cursor_num}) > a > img ') and cursor_num < 30:
    temp = driver.find_element(By.CSS_SELECTOR,f'body > main > div.container > div:nth-child({cursor_num}) > a').get_attribute("href")
    print(temp)
    driver.quit()
    driver.implicitly_wait(3)
    driver.get(temp)
    turl=driver.find_element(By.CSS_SELECTOR,'body > main > div.container > div:nth-child(7) > img').get_attribute("src")
    print(turl)
    response=requests.get(turl,stream=True)
    cursor_num+=1
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
            data=str(taglabel['UserComment'])
            data=data.replace("b'UNICODE",'')
            data=data.replace("\\x00",'')
            take=data.split('\\n')

            #get prompt
            #prompt=take[0]
            dict["prompt"]=take[0]
            #get negative
            negative=take[1].split(':')
            try:
                ne_prom=negative[1]
                for neg in negative[2:]:
                    ne_prom=ne_prom+':'+neg
                dict["negative"]=ne_prom
                #print(ne_prom)
                #get data
            except:
                dict["negative"]=ne_prom
            else_data=take[2].replace('\'','')
            else_data=else_data.replace(' ','')
            else_data=else_data.split(',')
            for eld in else_data:
                if ':' in eld:
                    datakey,datavalue = eld.split(':')
                    dict[datakey]=datavalue
            print(dict)
            temp_dic=["admin",turl,turl,dict['prompt'],dict['negative']if "negative" in dict else "NULL","NULL",dict['Steps'] if "Steps" in dict else "NULL",
                    dict['Sampler'] if "Sampler" in dict else "NULL",dict['CFGscale'] if "CFGscale" in dict else "NULL",dict['Seed'] if "Seed" in dict else "NULL",
                    dict['Modelhash'] if "Modelhash" in dict else "NULL",dict['Clipskip'] if "Clipskip" in dict else "NULL",dict['Denoisingstrength'] if "Denoisingstrength" in dict else "NULL"]
            diction.append(temp_dic)
    else:
        print("non")
    driver.quit()
    driver.implicitly_wait(3)
    driver.get(url)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')

#print
df=pd.DataFrame(diction)
df.to_excel('data.xlsx',header=head)
