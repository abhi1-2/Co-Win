import requests
import json
from json import JSONDecodeError
import os
import time
import datetime
district_id = '294'
date= datetime.datetime.today().strftime('%d-%m-%Y')
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id="+district_id+"&date="+date

payload={}
headers = {
  'authority': 'cdn-api.co-vin.in',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
  'accept': 'application/json, text/plain, */*',
  'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJiZjE1OWM0ZS00NzM5LTQxMjctYmNjNS1kODgxMjE1Mzc0MWQiLCJ1c2VyX2lkIjoiYmYxNTljNGUtNDczOS00MTI3LWJjYzUtZDg4MTIxNTM3NDFkIiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo4ODg0MzU2NTIzLCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjE3NDAzNzY4MTE4MDMwLCJzZWNyZXRfa2V5IjoiYjVjYWIxNjctNzk3Ny00ZGYxLTgwMjctYTYzYWExNDRmMDRlIiwidWEiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMF8xNV83KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTAuMC40NDMwLjkzIFNhZmFyaS81MzcuMzYiLCJkYXRlX21vZGlmaWVkIjoiMjAyMS0wNS0wN1QxMDo0NjowNy45MThaIiwiaWF0IjoxNjIwMzg0MzY3LCJleHAiOjE2MjAzODUyNjd9.07dz-rvmGgUbBl1b7X6GbzOPRHrf1CHpRLDyFm3hsEo',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
  'origin': 'https://selfregistration.cowin.gov.in',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://selfregistration.cowin.gov.in/',
  'accept-language': 'en-US,en;q=0.9'
}

print(date)
while 1:
    try:
        time.sleep(10)
        response = requests.request("GET", url, headers=headers, data=payload)
        available_centers = json.loads(response.text)
        
        for c in available_centers['centers']:
                for session in c['sessions']:
                    if(session['min_age_limit']==18  and session['available_capacity']>0):
                        os.system('say "appointment found please check"')
                        # send_otp_req()
                        print(c['name']+':  '+str(c['pincode']))
                        print(session) 
    except JSONDecodeError:
        print(response.text)
