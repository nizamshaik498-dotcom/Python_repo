#program made using datetime module.(combined)

from datetime import datetime, time, date
d=date(2024,2,5)
t=time(23)
combined=datetime.combine(d,t)
print(combined)