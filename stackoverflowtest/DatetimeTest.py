import datetime
from time import gmtime, strftime, localtime
print gmtime()
print strftime("%a, %d %b %Y %H:%M:%S +0530", localtime())


print str(datetime.date.today().strftime("%Y-%m-%d %H:%M"))

time_object = datetime.time()
print str(datetime.time.strftime(time_object, "%Y-%m-%d %H:%M"))

year,month,date_today = str(datetime.date.today().strftime("%Y-%m-%d")).split('-')
print year,month,date_today
datetime_object = datetime.datetime(int(year), int(month), int(date_today))
print datetime_object.hour
#print datetime_object.strptime()

print str(datetime.date.today())



