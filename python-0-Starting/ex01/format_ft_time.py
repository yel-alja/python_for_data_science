import time
import datetime

print("Seconds since January 1, 1970:" , time.time())
date = datetime.datetime.now().strftime("%b %d %Y")
print(date) 