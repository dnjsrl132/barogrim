from selenium import webdriver
from bs4 import BeautifulSoup
import requests

url="https://www.ptsearch.info/articles/list_best/"
driver=webdriver.Safari()
driver.get(url)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
links=soup.find_all('a')
#browser.quit()
n=1
for link in links:
	if n>100:
		break
	n+=1
	if n<50:
		continue
	href=link.get('href')
	print(href)

