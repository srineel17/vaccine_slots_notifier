# vaccine_slots_notifier
This is a polling script for determining the slot availability in real time

## Steps:

####1. Download and install python 3.* from below location, make sure to tick the 'add python to PATH' at the time of installation
	
* url: https://www.python.org/downloads/


####2. Verify your installation, open 'cmd' and run the below command
	
* python --version

* It should pop up the version of python installed, anything else would be a reason for failure, please try installing again.


####3. In cmd prompt please run the below commands, copy-paste the commands
	
* pip install requests
* pip install playsound


####4. Move to the file location where the zip file is exported and run the booking script with below command

* python vaccination_slots_notifier.py


## NOTE: Script will ask for district id, which can be found from below URLS,

* state_info_url: https://cdn-api.co-vin.in/api/v2/admin/location/states,
* district_info_url: https://cdn-api.co-vin.in/api/v2/admin/location/districts/<enter_your_state_id_here>

