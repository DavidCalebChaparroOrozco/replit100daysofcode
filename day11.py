number_of_days_this_year = int(input("How many days are in this year?: "))

hours_per_day = 24
minutes_per_hour = 60
seconds_per_minute = 60

if number_of_days_this_year == 366:
  days_in_year = number_of_days_this_year
else:
  days_in_year = 365

seconds_in_year = days_in_year * hours_per_day * minutes_per_hour * seconds_per_minute

print(f"Number of seconds in one year with {number_of_days_this_year} days: {seconds_in_year}")
