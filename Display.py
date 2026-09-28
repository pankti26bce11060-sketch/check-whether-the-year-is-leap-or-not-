def display_result(year, leap, days, hours, minutes, seconds):
  print("\n----- year calculation result ----")
  if leap:
    print(f"{year} is a leap year.")
  else:
    print(f"{year} is not a leap year.")
  print(f"total days: {days}")
  print(f"total hours: {hours}")
  print(f"total minutes: {minutes}")
  print(f"total seconds: {seconds}")
