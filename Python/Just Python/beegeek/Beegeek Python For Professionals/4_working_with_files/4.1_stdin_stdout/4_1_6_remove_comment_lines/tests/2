import sys
from datetime import date

lis = [date(int(data.split('.')[2]), int(data.split('.')[1]), int(data.split('.')[0])) for data in sys.stdin]
new_lis = sorted(lis, key=lambda d: d.toordinal())
if new_lis == lis:
    print("###")
elif new_lis == lis[::-1]:
    print("DESC")
else:
    print("MIX")