#run this only if the main.py is giving 401 errors

from subprocess import call
import os

username = "vandyyuva"
start_year = 2023
start_month = 8
custom_date_utc = "datetime("+str(start_year)+", " + str(start_month) + ", 1)"
second_arg = '--post-filter="date_utc <=' + custom_date_utc + '"'
call(["instaloader", second_arg, username])
