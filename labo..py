# import os
# import requests
# import pandas as pd
# import json
# from pprint import pprint
# from dotenv import load_dotenv
# load_dotenv()
import scw



# API_TOKEN = os.getenv("wearther_api")
# ApiKey = API_TOKEN # 各自で取得した Key を設定する


# print("="*25)

# def ch(world_name):
#     url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=ja&units=metric&appid={API_key}"
#     url = url.format(city_name = world_name, API_key = ApiKey)
#     jsondata = requests.get(url).json()
#     weather = jsondata["weather"][0]["description"]

#     #print(weather_splt)
#     ################################################
#     #---------------------#
#     #絵文字を追加する
#     if jsondata["name"] == ("東京都"): print(f'【地域：{jsondata["name"]}🇯🇵 】')
#     elif jsondata["name"] == ("神奈川県"): print(f'【地域：{jsondata["name"]}🇯🇵 】')
#     elif jsondata["name"] == ("Phuket"): print(f'【地域：{jsondata["name"]}🇯🇹🇭 】')
#     elif jsondata["name"] == ("カナダ"): print(f'【地域：{jsondata["name"]}🇨🇦 】')
#     elif jsondata["name"] == ("アムステルダム"): print(f'【地域：{jsondata["name"]}🇳🇱 】')
#     #---------------------#
#     if list(weather).count("雲"): 
#         print(f'  上空：{weather}だお🌥')
#     elif list(weather).count("晴"): 
#         print(f'  上空：{weather}だお🌞')
#     elif list(weather).count("雨"): 
#         print(f'  上空：{weather}だお☔️')
#     elif list(weather).count("雪"): 
#         print (f'  上空：{weather}だお☃️')
#     #---------------------#
#     #続き！
#     print(f'  気温：{jsondata["main"]["temp"]}°')
#     print(f'  体感：{jsondata["main"]["feels_like"]}°')
#     print(f'  最低：{jsondata["main"]["temp_min"]}°')
#     print(f'  最高：{jsondata["main"]["temp_max"]}°')
#     print(f'  気圧：{jsondata["main"]["pressure"]}hPa')
#     print(f'  湿度：{jsondata["main"]["humidity"]}%')
#     print(f'  風速：{jsondata["wind"]["speed"]}km')
#     return ("="*25)

# if __name__ == '__main__':
#     # world = {"東京":[43.0642, 141.3469], "プーケット":[7.8906, 98.3981],  "カナダ": [60.1087, -113.6426], "アムステルダム":[52.374, 4.8897]}
#     #world = ['Tokyo, JP']
#     world = ['Tokyo, JP','Kanagawa, JP','Phuket, TH','Canada, CA','Amsterdam, NL',]
#     for x in range(len(world)):
#         print(scw.ch(world_name=world[x]))
    


print(scw.result())
    









    

