pi = 31.4159265
print ("%.4e" % (pi))
day = 14
month = 2
year = 2012
hours = 16
minutes = 20
seconds = 50
print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))
# 2012/14/2
print("%2d:%2d:%2d" % (hours, minutes, seconds))