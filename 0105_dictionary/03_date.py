import datetime

print(datetime.datetime.now())
today = datetime.date(2023,1,5)
print(type(today))
print(today.year)
print(today.day)

end = datetime.date(2023,6,14)
print(end-today)