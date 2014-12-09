from app import write_entries
import datetime
import random

ts = datetime.datetime.now().strftime("%Y-%m-%d%H:%M-%S")
offset = random.randrange(0, 1475)

print("Enter user=%s" % ts)
print("Enter email=%s" % offset)
prime = write_entries.delay(ts, offset)
