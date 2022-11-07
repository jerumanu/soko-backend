from flask import requests

payload={'lat':40,'lon':-105}

payload['lat']=30

payload['lon']=80

#print(r['inputs']['log'])
print (payload)
r=requests.get('https://developer.nrel.gov/api/pvwatts/v6.json?api_key=DEMO_KEY&system_capacity=4&azimuth=180&tilt=40&array_type=1&module_type=1&losses=10', params=payload).json()


print('latitude of the area',
  r['inputs']['lat']
  
)

print(r['inputs']['log'])
print('annual psh of the area',r['outputs']["solrad_annual"])
print("psh of the area",r['outputs']["solrad_monthly"])
PSH=min(r["outputs"]["solrad_monthly"])

