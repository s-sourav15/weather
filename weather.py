from selenium import webdriver
from collections import defaultdict
links=["https://weather.com/weather/today/l/3c9c76946dbd3a4284d0e28257dc0535231cbc97e4101e3f648a70180c5417a1","https://weather.com/weather/today/l/76781bbe926ce0ef9d8a1442563922e6f65c20c8b997c32a4d3e1e3dcfa400f7"]

f=open('seed_weather.txt','r')
lines=f.readlines()
count=0
# print(lines)

vals=[]
val_future=[]
val_side=[]
for link in lines:
    driver = webdriver.Chrome('/Users/soumyasourav/Downloads/chromedriver')
    # driver.close()
    # print(link)
    driver.get(link)
    # print(driver)
    # driver.implicitly_wait(10)
    element_main=driver.find_element_by_class_name('today_nowcard-main')
    element_future=driver.find_element_by_id('LookingAhead')
    # element_title=driver.find_element_by_class_name('warning-text')
    element_side=driver.find_element_by_class_name('today_nowcard-sidecar')

    # print(element_title)
    # driver.fin
    vals.append(element_main.text)
    val_future.append(element_future.text)
    val_side.append(element_side.text)
    driver.close()

# print(vals)
weather=defaultdict(list)
side=defaultdict(list)
future=defaultdict(list)
for val in val_side:
    # print('side')
    x=(val.strip().split('\n'))
    side['Wind'].append(x[2])
    side['Humidity'].append(x[4])
    side['Dew Point'].append(x[6])
    side['Pressure'].append(x[8])
    side['Visibility'].append(x[10])
for val in val_future:
    # print('future')
    x=(val.strip().split('\n'))
    future['time_frame'].append(x[0])
    # future['tonight'].append(x[2])
    future['tonight_conditions'].append({'tonight':x[3],'low':x[5],'precipitation_chance':x[6]})
    future['tomorrow_conditions'].append({'high':x[9],'low':x[13],'precipitation_chance':x[10]})
    future['day_after_tomorrow_conditions'].append({'high': x[17], 'low': x[21], 'precipitation_chance': x[22]})
for val in vals:

    x=val.strip().split('\n')
    weather['location'].append(x[0])
    weather['time'].append(x[1])
    weather['temp'].append(x[2])
    weather['condition'].append(x[3])
    weather['feels_like'].append(x[4])
    weather['high_low'].append(x[5])
    weather['uv'].append(x[6])
    weather['warnings'].append(x[7])
    # print(x)

print(weather)
# driver.find_element_by_id('today_nowcard-main').send_keys('.')
print(side)
print(future)
import json

fi=open('weather_data.json','a')
json.dump(weather,fi)
json.dump(future,fi)
json.dump(side,fi)
# #
