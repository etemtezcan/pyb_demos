import sys
import pyb
rtc = pyb.RTC()
rtc.datetime((2014, 8, 5, 2, 14, 40, 0 , 0))
a = rtc.datetime()
name = '0:/{}_{}_{}_{}_{}.csv'.format(a[0],a[1],a[2],a[4],a[5])
log = open(name, 'w')
log.close()