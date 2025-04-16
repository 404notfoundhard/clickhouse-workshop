#!/usr/bin/env python
from random import randint
from datetime import date
from datetime import datetime
import time

for xx in range(1,2):
    start = int(time.time())
    end = int(time.time()) + 5000000
    offset = 10 
    data_to_csv = []
    print('make test_data'+str(xx)+'.csv')
    with open('./test_data'+str(xx)+'.csv','w') as f:
        while start <= end:
            for i in range(1,10):
                timestamp = datetime.fromtimestamp(start).strftime("%Y-%m-%d %H:%M:%S")
                date = datetime.fromtimestamp(start+randint(-4678400,4678400)).date().strftime("%Y-%m-%d")
                applicationId = str(randint(1000000000000000000,3096457873352262913))
                my_interval = str(randint(1,86121))
                count = str(randint(1,30))
                f.writelines(","+"\""+timestamp+"\","+applicationId+",\""+date+"\","+my_interval+","+count+"\n")
            start += (offset + randint(0,50))
