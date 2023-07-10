import pymysql
import time
import datetime


def picture_insert(conn,cursor, dict, name):


    ts = time.time()
        
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    # temp_negative = dict['ori_negative_prompt'][2:].replace("'","\\'")



    sql = f'''INSERT INTO picture_data (user_id, name, file_link, prompt, negative_prompt,timestamp,steps,sampler,cfg_scale,seed,model_hash,clip_skip,denoising_strength) 
    VALUES ("admin","{name}","{name}","{dict['ori_positive_prompt']}","{dict['ori_negative_prompt'] if 'ori_negative_prompt' in dict else "NULL"}",
    "{timestamp}",{dict['Steps'] if 'Steps' in dict else "NULL"} ,"{dict['Sampler'] if 'Sampler' in dict else "NULL"}",
    {dict['CFG scale'] if 'CFG scale' in dict else "NULL"},{dict['Seed'] if 'Seed' in dict else "NULL"},
    "{dict['Model hash'] if 'Model hash' in dict else "NULL"}",{dict['Clip skip'] if 'Clip skip' in dict else "NULL"},
    {dict['Denoising strength'] if 'Denoising strength' in dict else "NULL"});'''
    
    # '{dict['Steps']}','{dict['Sampler']}','{dict['ori_positive_prompt']}','{dict['CFG scale']}','{dict['Seed']}','{dict['Model hash']}','{dict['Clip skip']}','{dict['Denoising strength']}',{timestamp}
    
    print("sql :",sql)

    cursor.execute(sql)
    conn.commit()

conn = pymysql.connect(host='15.164.231.65', port=51143, user='grim', password='1111', db='grim', charset='utf8')
cursor = conn.cursor()

