#Import modules
import datetime
import bday_messages

#Variables
#Today
date1 = datetime.date.today()
#Date of next birthday
date2 = datetime.date(1999, 9, 24)
 #Calculate time difference between dates
time_difference = date2 - date1
#Calculate days away to next birthday
days_away = time_difference.days % 365

print(date1)
print(date2)

bday_date = date2.replace(year=date1.year)

if date1 == bday_date:
    print(bday_messages.random_message)
else:
    print(f'Your next birthday is {days_away} days away!')

