import urllib.request as r
import json
import collections
import itertools
jsonurl = r.urlopen('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')
text = json.loads(jsonurl.read()) # <-- read from it
data=text['data']
#print(len(data['stations']))   664 stations
#print(data['stations'][0]['station_id']) # station id

# station id Extract:
total_stations_id = []
for i in range(len(data['stations'])):
    id=data['stations'][i]['station_id']
    total_stations_id.append(id)
total_stations_id=[int(x) for x in total_stations_id]
print('station_id list:'+str(total_stations_id))
# num_bikes_available Extract:
total_num_bikes_available = []
for i in range(len(data['stations'])):
    num_bikes_available = data['stations'][i]['num_bikes_available']
    total_num_bikes_available.append(num_bikes_available)
print('bikes availble:'+str(total_num_bikes_available))
# num_docks_available Extract:
total_docks_available = []
for i in range(len(data['stations'])):
    docks_availble=data['stations'][i]['num_docks_available']
    total_docks_available.append(docks_availble)
print('docks availble:'+str(total_docks_available))
total_docks=[x + y for x, y in zip(total_num_bikes_available, total_docks_available)]
print('total docks for each station:'+str(total_docks))
#to_dict
new_dict = dict(zip(total_stations_id,total_docks))
print('zip station_id and total docks:'+str(new_dict))

file = open('total_docks_per_station.txt','w')
file.write(str(new_dict))