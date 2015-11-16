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
