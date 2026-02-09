#program made using datetime module.(replace)

from datetime import datetime
now=datetime.now()
new_date=now.replace(year=2025, month=2,day=5)
print(new_date)
