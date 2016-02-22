#UNFINISHED
import datetime
from itertools import product
n = int(input())
#def daterange(start_date, end_date):
#   for n in range(int ((end_date - start_date).days)):
#        yield start_date + timedelta(n)
second = datetime.timedelta(seconds = 1)
day = datetime.timedelta(days = 1)
times = []
time = datetime.datetime(2000, 1, 1, 0, 0, 0)
while time.day == 1:
    times.append({'h': str(time.hour%12),
                  'hh': "{:02}".format(time.hour),
                  'H' : str(time.hour),
                  'HH' : "{:02}".format(time.hour),
                  'mm' : "{:02}".format(time.minute),
                  'ss' : "{:02}".format(time.second)})
    time = time + second
print(len(times))
print(times[-1])

def timecombos(components):
    return {components['h']+components['mm']+components['ss'], components['hh']+components['mm']+components['ss'], components['H']+components['mm']+components['ss'], components['HH']+components['mm']+components['ss']}

alltimecombos = [x for l in [timecombos(c) for c in times] for x in l]

def datecombo(M, MM, d, dd, yyyy, yy):
    return {'{}{}{}'.format(*x) for x in {(M,d,yy), (MM,d,yy), (M,dd,yy), (MM,dd,yy), (M,d,yyyy), (MM,d,yyyy), (M,dd,yyyy), (MM,dd,yyyy), (d,M,yy), (d,MM,yy), (dd,M,yy), (dd,MM,yy), (d,M,yyyy), (d,MM,yyyy), (dd,M,yyyy), (dd,MM,yyyy)}}
for _ in range(n):
    year = int(input())
    time = datetime.datetime(year, 1, 1, 0, 0, 0)
    while time.minute == 0:
        M = time.month
        MM = "{:02}".format(M)
        d = time.day
        dd = "{:02}".format(d)
        yyyy = time.year
        yy = str(yyyy)[-2:]
        for date_, time_ in product(datecombo(M,MM,d,dd,yyyy,yy), alltimecombos):
            if date_+time_ == reversed(date_+time_):
                print(date_+time_)
        
        
        time = time + day
    
