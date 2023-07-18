import requests
from PIL import Image
from PIL.ExifTags import TAGS
import time
import datetime
from view.models import CivitTest
home="http://127.0.0.1:8000/"
# Create your views here.
def Exif(url,user_id):
    
    #response=requests.get(url,stream=True)
    name_id=home+url
    name_=name_id.split('/')
    name_=name_[len(name_)-1]
    image=Image.open(url)
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
        temp_dic=[user_id,name_,name_id,dict['prompt'],dict['negative']if "negative" in dict else "NULL",dict['Size'] if "Size" in dict else "NULL",
                              dict['Steps'] if "Steps" in dict else "NULL",dict['Sampler'] if "Sampler" in dict else "NULL",dict['CFGscale'] if "CFGscale" in dict else "NULL",
                              dict['Seed'] if "Seed" in dict else "NULL",dict['Modelhash'] if "Modelhash" in dict else "NULL",
                              dict['Clipskip'] if "Clipskip" in dict else 0,dict['Denoisingstrength'] if "Denoisingstrength" in dict else "NULL"]
        
        new_posts=CivitTest()     
        new_posts.user_id = temp_dic[1]
        new_posts.name = temp_dic[2]
        new_posts.file_link = temp_dic[2]
        new_posts.prompt = temp_dic[3]
        new_posts.negative_prompt = temp_dic[4]
        ts=time.time()
        new_posts.timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        new_posts.steps = temp_dic[6]
        new_posts.sampler = temp_dic[7]
        new_posts.cfg_scale = temp_dic[8]
        new_posts.seed = temp_dic[9]
        new_posts.model_hash = temp_dic[10]
        new_posts.clip_skip = temp_dic[11]
        new_posts.denoising_strength = temp_dic[12]
        
    new_posts.save()
    return 0
