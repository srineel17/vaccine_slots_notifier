import requests
import time
from datetime import datetime, timedelta, date
import json
import winsound
from playsound import playsound

def slot_by_district(district_id, dose):

    while True:

        cdate = (date.today() + timedelta(days=1)).strftime("%d-%m-%Y")
        req_url =  'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict' +'?district_id=' + district_id + '&date=' + cdate

        response = requests.get(
                            req_url,
                           # headers={'Accept-Language':'en_US','accept': 'application/json'},
                           headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},
                   )

        content = response.json()

        if dose == 1:
            available_slots = sorted([i for i in content['sessions'] if i['available_capacity'] > 0 and i['min_age_limit'] == 18 ], key = lambda i: i['available_capacity'], reverse=True)
        elif dose == 2:
            available_slots = sorted([i for i in content['sessions'] if i['available_capacity_dose2'] > 0 and i['min_age_limit'] == 18 ], key = lambda i: i['available_capacity_dose2'], reverse=True)

        if len(available_slots) > 0:
            playsound('./beep-24.mp3')
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
            print()
            print("date and time =", dt_string)
            print()
            for i in available_slots:
                if i['fee_type'] == 'Paid':
                    print(str(i['pincode']) + ' | ' + str(i['vaccine']) + ' | '  + str(i['fee_type']) + ' - \u20B9' + str(i['fee']) + ' | ' + str(i['date']) + ' | ' + str(i['available_capacity']).zfill(3) + ' | ' + str(i['min_age_limit']) + ' | ' + str(i['name']) + ' | ' + str(i['address']))
                else:
                    print(str(i['pincode']) + ' | ' + str(i['vaccine']) + ' | '  + str(i['fee_type']) + ' | ' + str(i['date']) + ' | ' + str(i['available_capacity']).zfill(3) + ' | ' + str(i['min_age_limit']) + ' | ' + str(i['name']) + ' | ' + str(i['address']))
            print('-------------------------------------------------------------------------------------------------------------')

        time.sleep(5) #Time interval between number of hits in value seconds, minimum value should be 3 (Government allows 100 hits every 5 mins)


district_id = str(input("Please enter your District's ID: "))
dose = int(input("Dose 1 or Dose 2 (Enter 1/2): "))

slot_by_district(district_id, dose) #Input Parameter is district_id
