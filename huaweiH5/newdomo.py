import datetime

date = datetime.datetime.now().strftime('%d日')
a = datetime.datetime.now().timetuple()
VersionInfo = str(a.tm_mon)+"月"+date
print(VersionInfo)