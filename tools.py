import requests as rq
import json


class rq_ra():
  ra=rq.get('https://private-anon-589c768a77-popcornofficial.apiary-proxy.com/random/anime')
  ra1=rq.get('https://tv-v2.api-fetch.website/random/anime')
  text=ra1.text
  rq_json=json.loads(text)
  title=rq_json['title']
  
class Weather():
  opwm=''
  url=''
  r=rq.get(url).text
  r_json=json.loads(r)
  