#coding:utf-8

import time
from datetime import date
import datetime

begin = time.time()
print("debut")
time.sleep(5)
end = time.time()
print("fin")
print("temps du debut : ",begin)
print("temps du fin :",end)
print(begin - end)

d1 = datetime.datetime(2018,2,28,13,30,2)
d2 = datetime.datetime(2018,2,27,13,30,2)
print(d1)

if d1 < d2:
    print("d1 est plus ancien que d2")
else: print("d1 est plus recent que d2") 
print(date.today())