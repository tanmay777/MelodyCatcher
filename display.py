from __future__ import print_function

import timeit
import sys
x=0
'''while x<50000:
    start_time=timeit.default_timer()
    end_time=timeit.default_timer()
    sys.stdout.write('\rTimer: ' + str(end_time - start_time))
    x=x+1'''
x=30.239345
print("%.2f" %x)


