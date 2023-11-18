import os
import requests
import pandas as pd
import json
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv("wearther_api")
ApiKey = API_TOKEN # 各自で取得した Key を設定する
######################################################

def ch(world_name):

    box = []
    url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=ja&units=metric&appid={API_key}"
    url = url.format(city_name = world_name, API_key = ApiKey)
    jsondata = requests.get(url).json()
    weather = jsondata["weather"][0]["description"]

    #print(weather_splt)
    ################################################
    #---------------------#
    #絵文字を追加する
    box.append("="*18)
    if jsondata["name"] == ("東京都"): box.append(f'【地域：{jsondata["name"]} 🇯🇵 】')
    elif jsondata["name"] == ("神奈川県"): box.append(f'【地域：{jsondata["name"]} 🇯🇵 】')
    elif jsondata["name"] == ("Phuket"): box.append(f'【地域：{jsondata["name"]} 🇹🇭 】')
    elif jsondata["name"] == ("カナダ"): box.append(f'【地域：{jsondata["name"]} 🇨🇦 】')
    elif jsondata["name"] == ("アムステルダム"): box.append(f'【地域：{jsondata["name"]} 🇳🇱 】')
    #---------------------#
    if list(weather).count("雲"): box.append(f'  上空：{weather}だお🌥')
    elif list(weather).count("晴"): box.append(f'  上空：{weather}だお🌞')
    elif list(weather).count("雨"): box.append(f'  上空：{weather}だお☔️')
    elif list(weather).count("雪"): box.append(f'  上空：{weather}だお☃️')
    #---------------------#
    #続き！まとめて追加！
    box.extend([(f'  気温：{jsondata["main"]["temp"]}°'), (f'  体感：{jsondata["main"]["feels_like"]}°'), (f'  最低：{jsondata["main"]["temp_min"]}°'), 
               (f'  最高：{jsondata["main"]["temp_max"]}°'),  (f'  気圧：{jsondata["main"]["pressure"]}hPa'), (f'  湿度：{jsondata["main"]["humidity"]}%'),
               (f'  風速：{jsondata["wind"]["speed"]}km')])
    return box

#----------------------------------------------------

def result():

    world = ['Tokyo, JP','Kanagawa, JP','Phuket, TH','Canada, CA','Amsterdam, NL',]
    #world = ['Tokyo, JP','Kanagawa, JP']
    # テキストを空にする！
    with open("myfile.txt", "w") as f:
        pass
    # 全てのworldの天気をテキストに書き込む！
    for j in world:
        for i in range(0,10):    
            # 書き込み用配列作成
            contents = [ch(world_name=j)[i]]
            # 1行ずつ書き込み #mode='a'は追加書き込み
            with open('myfile.txt', mode='a', encoding='utf-8', newline='\n') as f:
                for content in contents:
                    f.write(content + "\n")
                f.close()
    with open("myfile.txt", encoding="UTF-8") as f:
        text = f.read()
    return (text)
######################################################
#world = {"東京":[43.0642, 141.3469], "プーケット":[7.8906, 98.3981],  "カナダ": [60.1087, -113.6426], "アムステルダム":[52.374, 4.8897]}
#world = ['Tokyo, JP']
#world = ['Tokyo, JP','Kanagawa, JP','Phuket, TH','Canada, CA','Amsterdam, NL',]
# if __name__ == "__main__":
######################################################
        
    
    

