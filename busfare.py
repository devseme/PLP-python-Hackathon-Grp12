import datetime as dt
import calendar
# gets todays date and stores it as variable date
date=dt.date.today()

# print("Today`s day:" ,date.day)

# getting day name,capitalizing first letter and getting first 3 characters
today=calendar.day_name[date.weekday()].capitalize()[0:3]


# elif condition to check day of week for respective fare prices
if (today==0,1,2,3,4): 
    fare=100
   
elif(today==5):
    fare=60
    
elif(today==6):
    fare=80
      
else:
    print("invalid day")    
    
print("Date:" ,date)     
print("Fare:" ,fare)   
print("Day:" , today)