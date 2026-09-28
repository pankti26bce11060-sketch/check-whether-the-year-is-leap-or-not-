from leap_year import
check_leap_year
def calculate_time(year):
  if check_leap_year(year):
    days = 366
  else:
    days = 365
  hours = days * 24
  minutes = hours * 60
  seconds = minutes * 60
  return days, hours, minutes, seconds
