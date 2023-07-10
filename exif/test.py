from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from PIL import Image
from PIL.ExifTags import TAGS
import requests
import pandas as pd

def check(driver):
    try:
        turl=driver.find_element(By.CSS_SELECTOR,'body > main > div.container > div:nth-child(7) > img').get_attribute("src")
    except:
        turl="NULL"
    return turl

week_start=37
home = "https://www.ptsearch.info"
url="https://www.ptsearch.info/articles/list_best/"
data=[]
driver=webdriver.Safari()
driver.get(url)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
links=soup.find_all('a')
for week in range(37):
    diction=[]
    for page in range(4):
        url="https://www.ptsearch.info/articles/list_best/?page="+str(page+9)+"&week="+str(week_start-week)
        print(url)
        driver.get(url)
        if driver.title=="Not Found":
            break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')

        cursor_num=2   #cursor_num = 1
        
        head=["id","name","file_link","prompt","negative_prompt","size","steps","sampler","cfg_scale","seed","model_hash","clip_skip","denoising_strentgh"]

        #find pic
        while driver.find_element(By.CSS_SELECTOR,f'body > main > div.container > div:nth-child({cursor_num}) > a > img') and cursor_num < 30:
            print(url)
            temp = driver.find_element(By.CSS_SELECTOR,f'body > main > div.container > div:nth-child({cursor_num}) > a').get_attribute("href")
            print(temp)
            driver.get(temp)
            turl=check(driver)
            print(turl)
            cursor_num+=1
            driver.get(url)
df=pd.DataFrame(data)
df.to_excel('table_data.xlsx')



