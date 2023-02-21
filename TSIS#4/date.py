# Напишите программу на Python для вычисления разницы двух дат в секундах.
import datetime
date1 = datetime.datetime(2023, 2, 16, 12, 10, 50)
date2 = datetime.datetime(2023, 2, 18, 18, 18, 40) # 2day, 6:07:50 = 2*24*60*60 + 6*60*60 + 7*60 +50 = 172800+21600+420+50=194870
# delta = date2 - date1
# days = delta.days
seconds = (date2 - date1).total_seconds()
print(seconds)
