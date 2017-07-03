import sys
import os
import html
import random
import time

from datetime import datetime

mixed_array = ["GT940MX", 2017, 'a']
this_year = datetime.today().year

if this_year in mixed_array:
    print("Python using mixed-type array")
    print("No need for using curly braces to delimit blocks of code in Python")

for data in mixed_array:
    print(data)

for timeLoop in range(4):
    right_this_minute = datetime.today().minute
    if 1 == right_this_minute % 2:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute")
    time.sleep(random.randint(10, 60))
print(sys.platform + " " +  sys.version)
print(os.getcwd())
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)
print(html.escape("This HTML fragment contains <SCRIPT>DANGEROUS</SCRIPT> script"))