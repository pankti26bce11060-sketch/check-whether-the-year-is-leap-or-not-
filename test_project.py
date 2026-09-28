from leap_year import
check_leap_year
from calculator import
calculate_time
# Test leap years
assert  check_leap_year(2024) == True
assert check_leap_year(2000) == false
# Test non-leap years
assert check_leap_year(2023) == false
assert check_leap_year(1900) == false
# test calculations
days, hours, minutes, seconds = calculate_time(2024)
assert days == 366
assert hours == 8784
assert minutes == 527040
assert seconds == 31622400
print("All tests passed successfully!")
