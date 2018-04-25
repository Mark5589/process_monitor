'''
Created on 24 Apr 2018

@author: gal
'''
import psutil
from time import sleep

while True:
    dict1 = {}
    for p in psutil.process_iter():
        dict1[p.pid] = p.name(), p.status(), p.create_time()
        with open("process_list.csv", "a") as process_list:
            process_list.write(str(p.pid) + "," + p.name() + "," + str(p.create_time())+","+p.status())
            process_list.write("\r\n")
    # for i,value in dict1.items():
    #     print i,", value: " ,value
    dict2 = {}
    #     sleep(5)
    for p in psutil.process_iter():
        dict2[p.pid] = p.name(), p.status(), p.create_time()
        with open("process_list.csv", "a") as process_list:
            process_list.write(str(p.pid) + "," + p.name() + "," + str(p.create_time())+","+p.status())
            process_list.write("\r\n")

    value = {k: dict2[k] for k in set(dict2) - set(dict1)}
    if (value):
        for key, value1 in value.items():
            with open("Status_Log_File.csv", "a") as status_log:
                name, status, time = value1
                print "opend...."
                status_log.write(str(key) + "," + name + "," + "opened" + "," +str(time))
                status_log.write("\r\n")
        # with open("Status_Log_File.csv", "a") as Status_Log_File:  #
        #     Status_Log_File.write(l.getName() + "," + l.getPid() + "," + l.getCTime() + "," + "Closed")
        #     Status_Log_File.write("\r\n")
    value = {k: dict1[k] for k in set(dict1) - set(dict2)}
    if (value):
        for key, value1 in value.items():
            with open("Status_Log_File.csv", "a") as status_log:
                name, status, time = value1
                print "opaa closed...."
                status_log.write(str(key) + "," + name + "," + "closed" + "," +str(time))
                status_log.write("\r\n")

# def Matches(dict,key):
#     return dict.has_key(key)