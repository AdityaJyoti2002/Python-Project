import json
import os
import requests


city = input("Enter The name of the City: ")
Url = f"https://api.weatherapi.com/v1/current.json?key=a387c3aedc7c45ed99a95820232212&q={city}"

r = requests.get(Url)
# print(r.text)
wdic = json.loads(r.text)
# print(wdic['current']['temp_c'])
# w = [wdic['current']['temp_c']]
# os.system(f"say 'The Current weather in {city} is {w} degrees'")
if   'error' in wdic:
    print(f"sorry, {city} is not a valid city")
    # print(wdic['current']['temp_c'])
    # os.system(f"say 'The Current weather in {city} is {w} degrees'")
else:
    w = [wdic['current']['temp_c']]
    print(wdic['current']['temp_c'])
    os.system(f"say 'The Current weather in {city} is {w} degrees'")
    # print("sorry, {city} is not a valid city")
