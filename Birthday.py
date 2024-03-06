import datetime

print("roycarey2058")	
birthdate = input("What is your birthdate (MM/DD/YYYY)? ")

month, day, year = birthdate.split("/")
bdate = datetime.datetime(int(year), int(month), int(day))
todays_date = datetime.datetime.now()
age = todays_date - bdate

print ("You are " + str(age.days/365.25) + " years old")
 
