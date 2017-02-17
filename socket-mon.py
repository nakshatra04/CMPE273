import psutil
import random
from operator import itemgetter


class Network_Connection_Status:
    __pid = "pid"
    __laddr = "laddr"
    __raddr = "raddr"
    __status = "status"
    __noc = "No Of Connection"

    def __init__(self, pid, laddr, raddr, status, noc):
        self.__pid = pid
        self.__laddr = laddr
        self.__raddr = raddr
        self.__status = status
        self.__noc = noc

    def set_pid(self, value):
        self.__pid = value

    def set_laddr(self, value):
        self.__laddr = value

    def set_raddr(self,value):
        self.__raddr = value

    def set_status(self, value):
        self.__status = value

    def get_pid(self):
        return self.__pid

    def get_laddr(self):
        return self.__laddr

    def get_raddr(self):
        return self.__raddr

    def get_status(self):
        return self.__status


tc = psutil.net_connections()
count = len(tc)
firstobject = Network_Connection_Status("pid", "laddr", "raddr", "status","no of connection")

objectlist = []
print "\"", "pid", "\",\"", "laddr", "\",\"","raddr", "\",\"","status","\""


for x in range(count):
    temp = Network_Connection_Status(tc[x].pid, tc[x].laddr, tc[x].raddr, tc[x].status,0)
    if tc[x].status != 'NONE' and tc[x].status != 'LISTEN':
        objectlist.append([temp.get_pid() , temp.get_laddr(), temp.get_raddr(), temp.get_status(),temp,0])



nl = sorted(objectlist, key= itemgetter(0))
sl = []
count =1
for x in range(1,len(nl)):
    temp_pid = nl[x-1][0]
    if nl[x][0] == nl[x-1][0]:
        temp_pid = nl[x-1][0]
        count +=1
    else:
       sl.append([temp_pid,count])
       count = 1
sl.append([temp_pid,count])

i = 0
j = 0
for i in range(len(sl)):
    for j in range (len(nl)):
        if sl[i][0] == nl[j][0]:
            nl[j][5] = sl [i][1]

nl = sorted(nl,key=itemgetter(5))

for x in range(len(nl)):
    print "\"", nl[-(x+1)][4].get_pid(), "\",\"", nl[-(x+1)][4].get_laddr(), "\",\"",nl[-(x+1)][4].get_raddr(), "\",\"",nl[-(x+1)][4].get_status(),"\""
