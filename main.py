# lep year and time calculator
year = int(input("enter a year :"))
# check whether the year is leap year
if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
  days = 366
  print(year, "is  a leap year")
else:
  days = 365
  print(year,"is not a leap year")
# calculate total time
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
# display results
print("total number of days :")
print("total number of hours :")
print("total number of minutes :")
print("total number of seconds :")
