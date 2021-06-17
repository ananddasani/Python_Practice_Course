# improt time module and rename with use of "as" if any

import time as t

time_now = t.localtime()
print(time_now)

print("Transaction completed at -> " + str(time_now.tm_hour) +
      "h " + str(time_now.tm_min) + "m")

'''
It represents the point where time starts.
Python uses the Unix epic which is January 1st 1970 at zero hours zero minutes and zero seconds.
So what do we have here is the exact number of seconds elapsed since that day.
'''
print(t.time())

# sleep for 5 sec.
t.sleep(5)
