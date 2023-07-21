import requests
from PIL import Image
from PIL.ExifTags import TAGS




# Create your views here.
def Exif(image):
    
    #image=Image.open(url)
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
        temp_dic=["","","",dict['prompt'],dict['negative']if "negative" in dict else "NULL",dict['Size'] if "Size" in dict else "NULL",
                              dict['Steps'] if "Steps" in dict else "NULL",dict['Sampler'] if "Sampler" in dict else "NULL",dict['CFGscale'] if "CFGscale" in dict else "NULL",
                              dict['Seed'] if "Seed" in dict else "NULL",dict['Modelhash'] if "Modelhash" in dict else "NULL",
                              dict['Clipskip'] if "Clipskip" in dict else 0,dict['Denoisingstrength'] if "Denoisingstrength" in dict else "NULL"]
        
        
        #print(new_posts.img)
    return temp_dic
