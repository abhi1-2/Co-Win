# Co-Win
Hey guys, the pandemic has been hard on all of us and we all thought when the vaccine will be out we will be back to life as usual. Boy were we wrong 😩 .

Now that the vaccines are out getting an appointment is like winning a lottery escpecially for the age group 18-45.

## Problems with the CO-Win Website - 
  1. OTP verification fails half of the time.
  2. When opened on a mobile device initially the page is blank and on refreshing it takes you back to login page.
  3. As of May 8th 2021 most states have a shortage of vaccines . As a result most states are priortizing 45+ age group and slots for 18+ age group are rare and as of now only avalible with private hospitals.

So to help you guys out i wrote a mini script that informs you when an appointment is available in your district for a particular age group.

 ## Prerequisites for running the script - 
  1. A MacOS device . The srcipt was written for a Mac (will be updating the script to work on Windows as well)
  2. Python3 and some understandng of coding in python (this will help you tweak the program according to your needs)
 
## Steps to run the script - 
  1. Open Terminal
  2. Go to the folder with the directory name - Co-Win
  3. Now run the script cowin.py as follows - `python3 cowin.py`
  
That's it folks.
Once the scipt encounters an availble appointment you will get an automated voice notification with the message - <b>'Appointment found please check'</b>

Along with that in the terminal you can see the appointment information and the pincode that will help you locate the center.
e.g.
```console
Newbagalur Layout UPHC C 1:  560084
{'session_id': 'e3a84bd2-8785-42ab-8ffc-287f5d6231c3', 'date': '08-05-2021', 'available_capacity': 1, 'min_age_limit': 18, 'vaccine': 'COVAXIN', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-06:00PM']}
```

## Note

If you encounter too many - 
`Unauthenticated access!`
please update the authorization header with a new one.
