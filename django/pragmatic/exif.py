import requests
from PIL import Image
from PIL.ExifTags import TAGS
import time
import datetime
# Create your views here.
def Exif(url,user_id):
    new_posts=CivitTest()
    response=requests.get(url,stream=True)
    name_id=url.split('/')
    name_=name_id[len(name_id)-1]
    image=Image.open(response.raw)
    exif_data=image._getexif()
    taglabel={}
    dict={}
    if exif_data:
        for tag, value in exif_data.items():
            decoded = TAGS.get(tag,tag)
            taglabel[decoded]=value
        
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
        new_posts.user_id=user_id
        new_posts.name = url
        new_posts.file_link = url
        new_posts.prompt = dict['prompt']
        new_posts.negative_prompt = dict['negative']
        ts=time.time()
        new_posts.timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #steps
    
