import time
from datetime import datetime

d = 20 
s = d* 60*60*24
timestamp = time.mktime(datetime.today().timetuple()) + s
p = datetime.fromtimestamp(timestamp)
print(p)