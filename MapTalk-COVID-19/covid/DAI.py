import requests, json
from datetime import datetime
import time, DAN, requests, random
from cord import Cord as Cord


ServerURL = 'https://map.iottalk.tw' #with no secure connection
Reg_addr = 'COVIDTest' #if None, Reg_addr = MAC address

DAN.profile['dm_name'] = 'COVID-19'
DAN.profile['df_list'] = ['Confirmed-TI','Deaths-TI','Recovered-TI']
DAN.profile['d_name'] = 'COVID19Test' # None for autoNaming
DAN.device_registration_with_retry(ServerURL, Reg_addr)

time.sleep(10)

while True:
    try:
        website = requests.get('https://pomber.github.io/covid19/timeseries.json')
        site_json = json.loads(website.text)

        for key in Cord: 
            print(site_json[key][-1]['confirmed'],Cord[key]['name'],Cord[key]['lat'],Cord[key]['lng'],str(site_json[key][-1]['date']),datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            DAN.push ('Confirmed-TI', float(Cord[key]['lat']), float(Cord[key]['lng']), str(Cord[key]['name']), site_json[key][-1]['confirmed'], datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   
            time.sleep(1)
            print(site_json[key][-1]['deaths'],Cord[key]['name'],Cord[key]['lat'],Cord[key]['lng'],str(site_json[key][-1]['date']),datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            DAN.push ('Deaths-TI', float(Cord[key]['lat']), float(Cord[key]['lng']), str(Cord[key]['name']), site_json[key][-1]['deaths'], datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   
            time.sleep(1)

            print(site_json[key][-1]['recovered'],Cord[key]['name'],Cord[key]['lat'],Cord[key]['lng'],str(site_json[key][-1]['date']),datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            DAN.push ('Recovered-TI', float(Cord[key]['lat']), float(Cord[key]['lng']), str(Cord[key]['name']), site_json[key][-1]['recovered'], datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   
            time.sleep(1)


        
    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    
    print("sleep for 1 hour Zzzz....")   
    time.sleep(3600) #sleep 12 hour
