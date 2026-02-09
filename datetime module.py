#program made using date time module.

from datetime import datetime
now=datetime.now()
formatted_date=now.strftime('%A,%B,%d,%y')
print(formatted_date)