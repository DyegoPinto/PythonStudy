# %%

# import libraries

import datetime
# %%

# manipulating dates

dt_now = datetime.datetime.now()

print(dt_now)

dt = datetime.date.today()

print(dt)
# %%

year = dt.year 
month = dt.month
day = dt.day

print (f'year: {year}')
# %%

type(year)

dt_again = datetime.datetime(year,month,day)

print (dt_again)

dt_date = datetime.date(year,month,day)

print(dt_date)
# %%


time = dt_now.time()

print(time)
# %%

hour = time.hour
minute = time.minute
second = time.second

print (f'hour: {hour}:{minute}:{second}')
# %%

weekday = dt_now.strftime('%A')

print(weekday)

weeknumber = dt_now.strftime('%w')

print(weeknumber)

# %%

month_name = dt_now.strftime('%B')

print(month_name)

# %%

day_of_year = dt_now.strftime('%j')
#week_of_year = dt_now.strftime('%U')

print(day_of_year)
# %%

type(day_of_year)
# %%

# adding or substracting days to a date

day = 2

datetime.date.fromordinal(dt.toordinal()+day)
# %%
