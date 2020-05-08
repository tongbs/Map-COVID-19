import  requests, json
from cord import Cord as Cord
from datetime import datetime
#from bs4 import BeautifulSoup


website = requests.get('https://pomber.github.io/covid19/timeseries.json')
site_json = json.loads(website.text)
for key in Cord:
    print(key)
    print(site_json[key][-1]['confirmed'],Cord[key]['name'],Cord[key]['lat'],Cord[key]['lng'],datetime.now().strftime('%Y-%m-%d %H:%M:%S'))       
    print(site_json[key][-1]['date'])

#print(type(site_json))

#print(site_json['Taiwan*'][-1]['confirmed'])

