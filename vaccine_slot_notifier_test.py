import requests
import time
from datetime import datetime, timedelta, date
import json
import winsound
from playsound import playsound

def slot_by_district_local(district_id, pincode=None, age_limit=18):
    while True:
        cdate = (date.today() + timedelta(days=1)).strftime("%d-%m-%Y")
        print(cdate)
        
        f = open("ahmedabad_corporation_data.json")
        content = json.load(f)
        
        available_slots =  [i for i in content['sessions'] if i['pincode'] == pincode and i['available_capacity'] > 0 ]
                
        if len(available_slots) > 0:
            winsound.Beep(500, 500)
            playsound('./beep-24.mp3')
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
            print()
            print("date and time =", dt_string)
            print()
            for i in available_slots:
                print(str(i['pincode']) + ' | ' + str(i['vaccine']) + ' | '  + str(i['fee_type']) + ' | ' + str(i['date']) + ' | ' + str(i['available_capacity']) + ' | ' + str(i['min_age_limit']) + ' | ' + str(i['name']) + ' | ' + str(i['address']))
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            
        time.sleep(3) #Time interval between number of hits in value seconds, minimum value should be 3
    
district_id = str(input("Please enter your District's ID: "))        
pincode = int(input("Please enter your prefer pincode(Keep empty if you want to see all live slots in the district): "))
age_limit = int(input("Please enter your age preference ('18' for 18-44 | '45' for 45+): "))    

slot_by_district_local(district_id, pincode, age_limit)
