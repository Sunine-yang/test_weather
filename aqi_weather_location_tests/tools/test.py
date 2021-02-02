import time

from analysis.data_analysis import Data_analysis

print(Data_analysis.hour_time_handle(eval(str(int(time.time()))+'000')))
print(float(round(time.time(),3)))